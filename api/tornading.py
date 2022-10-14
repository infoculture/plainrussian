#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import signal
import fcntl
import time
import socket
from subprocess import Popen
import logging
import logging.handlers


# --- основные настройки
PORT = 9888
HOST = 'localhost'  # видно в top, htop, ps, etc
LOG_FILE = 'var/log/tornado.log'  # '' для отключения логирования
LOG_LEVEL = 'WARNING'  # INFO (все статусы), WARNING (>=404), ERROR (>=500)
# ---


# настраиваем логирование в файл
os.chdir(os.path.dirname(os.path.abspath(__file__)))
if LOG_FILE:
    try:
        os.makedirs(os.path.split(LOG_FILE)[0])
    except OSError:
        pass
    file_handler = logging.handlers.RotatingFileHandler(
        filename = LOG_FILE, mode='a+',  # имя файла
        maxBytes = 1000000,  # максимально байт в файле
        backupCount = 2)  # максимум файлов
    file_handler.setLevel(getattr(logging, LOG_LEVEL))
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s\t%(levelname)-8s %(message)s',
            datefmt = '%d-%m-%Y %H:%M:%S'))
    logging.getLogger('').setLevel(logging.NOTSET)
    logging.getLogger('').addHandler(file_handler)

# блокируемый файл для проверки активности сервера
PID_FNAME = 'var/log/' + (os.path.abspath(__file__).replace('/', '_')) + '.pid'
COMMANDS = ['start', 'stop', 'restart']


def daemon():
    logging.critical('--- SERVER (RE)STARTED')
    f = open(PID_FNAME, 'w')
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    f.write('%-12i' % os.getpid())
    f.flush()

    import tornado.httpserver
    import tornado.ioloop
    import tornado.wsgi

    #~ # настраиваем Джанго
    from readabilityio import application
#
#    container = tornado.wsgi.WSGIContainer(application) 
    http_server = tornado.httpserver.HTTPServer(application) 
    http_server.listen(PORT) 
    tornado.ioloop.IOLoop.instance().start() 


def start():
    started = alegry_started()
    if not started:
        pid = Popen([HOST, os.path.abspath(__file__), 'daemon'],
            executable='python').pid
        print 'Server started at port %s (pid: %i)...' % (PORT, pid)
    else:
        print 'Server alegry started (pid: %i)' % started


def stop():
    started = alegry_started()
    if started:
        os.kill(started, signal.SIGKILL)
        print 'Server stoped (pid %i)' % started
    else:
        print 'Server not started'


def restart():
    stop()
    time.sleep(1)
    start()


def alegry_started():
    '''
    Если сервер запущен, возвращает pid, иначе 0
    '''
    if not os.path.exists(PID_FNAME):
        f = open(PID_FNAME, "w")
        f.write('0')
        f.flush()
        f.close()

    f = open(PID_FNAME, 'r+')
    try:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        started = int(f.read())
    else:
        started = 0
    f.close()
    return started


if len(sys.argv) == 2 and sys.argv[1] in (COMMANDS + ['daemon']):
    socket.setdefaulttimeout(15)   
    cmd = sys.argv[1]
    globals()[cmd]()
else:
    print 'Error: invalid command'
    print 'Usage: python tornader.py {%s}.' % '|'.join(COMMANDS)
