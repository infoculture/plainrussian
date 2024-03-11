import json
import time

import tornado.web
import html2text
import requests

from pymongo import MongoClient, ASCENDING
from readability.readability import Document

from settings import MONGO_HOST, MONGO_PORT
from textmetric.metric import calc_readability_metrics


READ_DB = 'readability'
LOG_COLL = 'log'

ERROR_NONE = 0
ERROR_INVALID_DATA = 101


class RusMeasureHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.conn = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[READ_DB]
        self.log = self.db[LOG_COLL]
        self.log.create_index([("reqtime", ASCENDING)])

    def __log(self, logrec):
        self.log.insert_one(logrec)

    def get(self):
        rtime = time.time()
        url = self.get_argument('url')
        lang = self.get_argument('lang', 'ru')
        debug = self.get_argument('debug', "0")
        debug = int(debug) if debug.isdigit() else 0
        r = requests.get(url)
        ctype = r.headers['content-type'].lower() if 'content-type' in r.headers.keys() else 'text/html'
        print(ctype)
        ctype = ctype.split(';', 1)[0]
        if ctype == 'text/html':
            ht = html2text.HTML2Text()
            ht.ignore_links = True
            ht.ignore_images = True
            ht.ignore_emphasis = True
            text = ht.handle(Document(r.text).summary())
            status = ERROR_NONE
        elif ctype == 'text/plain':
            print(type(r.content))
            text = r.content.decode('utf8', 'ignore')
#            text = r.text.decode('utf8', 'ignore')
            status = ERROR_NONE
        else:
            text = None
            status = ERROR_INVALID_DATA
#        text = text.decode('utf8')
        if status == ERROR_NONE:
            results = calc_readability_metrics(text)
        else:
            results = {'lang' : lang, 'debug' : debug}
        if debug:
            results['debug'] = {'text' : text}
        results['status'] = status
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(results, indent=4))
        etime = time.time() - rtime
        logreq = results.copy()
        logreq['text'] = text
        logreq['reqtime'] = rtime
        logreq['time'] = etime
        self.__log(logreq)

    def post(self):
        rtime = time.time()
        text = self.get_argument('text')
        lang = self.get_argument('lang', 'ru')
        debug = self.get_argument('debug', "0")
        results = calc_readability_metrics(text)
        results['status'] = ERROR_NONE
        results['debug'] = debug
        results['lang'] = lang
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(results, indent=4))
        etime = time.time() - rtime
        logreq = results.copy()
        logreq['text'] = text
        logreq['reqtime'] = rtime
        logreq['time'] = etime
        self.__log(logreq)


application = tornado.web.Application([
    (r"/api/1.0/ru/measure/", RusMeasureHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9888)
    tornado.ioloop.IOLoop.instance().start()
