__author__ = "ibegtin"
from math import sqrt
import csv
import os

from numpy import mean, arange

from settings import BASE_DIR, TEXTSBYGRADE_FOLDER

TEXTSBYGRADE_PATH = os.path.join(BASE_DIR, TEXTSBYGRADE_FOLDER)

# Russian sounds and characters
RU_CONSONANTS_LOW = ["к", "п", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
RU_CONSONANTS_HIGH = ["б", "в", "г", "д", "ж", "з"]
RU_CONSONANTS_SONOR = ["л", "м", "н", "р"]
RU_CONSONANTS_YET = ["й"]

RU_CONSONANTS = RU_CONSONANTS_HIGH + RU_CONSONANTS_LOW + RU_CONSONANTS_SONOR + RU_CONSONANTS_YET
RU_VOWELS = ["а", "е", "и", "у", "о", "я", "ё", "э", "ю", "я", "ы"]
RU_MARKS = ["ь", "ъ"]
SENTENCE_SPLITTERS = [".", "?", "!"]
RU_LETTERS = RU_CONSONANTS + RU_MARKS + RU_VOWELS
SPACES = [" ", "\t"]

# List of prepared texts
TEXT_LIST = [
    ['text_ryaba.txt', 1, 'http://skazki.org.ru/tales/yaichko/', u'Курочка Ряба'],
    ['text_tale.txt', 1, 'http://www.books.kostyor.ru/tale55.html', u'Заколдованная королевна'],
    ['text_alyon.txt', 1, 'http://www.kostyor.ru/tales/tale44.html', u'Сказка. Финист - Ясный сокол'],
    ['text_barin.txt', 1, 'http://www.itup.ru/russkie-skazki/958-skazkaveshhij-son.html', u'Сказка: вещий сон'],
    ['text_doch.txt', 1, 'http://russkazka.narod.ru/dochipadcherica.html', u'Дочь и падчерица'],
    ['text_fox.txt', 1, 'http://skazles.ru/skazki/0020.html', u'Лиса и журавль'],
    ['tolstoy_lip.txt', 1, 'http://rvb.ru/tolstoy/01text/vol_10/01text/0076.htm', u'Толстой. Липунюшка'],
    ['bianki_murav.txt', 1, 'http://www.lib.ru/TALES/BIANKI/tohome.txt', u'Бианки. Как муравьишка домой спешил'],
    ['gaidar_kamen.txt', 1, 'http://www.lib.ru/GOLIKOW/gkamen.txt', u'Аркадий Гайдар. Горячий камень'],
    ['bianki_lesdom.txt', 1, 'http://www.lib.ru/TALES/BIANKI/lesdom.txt', u'Бианки. Лесные домишки'],

    ['text_whitebim.txt', 3, 'http://dog.adgth.ru/files/library/troepolsky_bim.htm', u'Гавриил Троепольский. '
                                                                                     u'Белый бим черное ухо.'],
    ['gaidar_stone.txt', 3, 'http://lib.ru/GOLIKOW/gkamen.txt', u'Гайдар. Горячий камень.'],
    ['steel_ring.txt', 3, 'http://books.rusf.ru/unzip/add-on/xussr_mr/paustk17.htm?1/1', u'Паустовский. '
                                                                                         u'Стальное колечко'],
    ['gaidar_countries.txt', 4, "http://skazki.russkay-literatura.ru/proizvedeniya-dlya-detej-ot-"
                                "8-let/224-dalnie-strany-gajdar-rasskaz.html",
     u'Гайдар. Дальние страны'],
    ['gaidar_baraban.txt', 4, 'http://ruslit.traumlibrary.net//book/gaydar-ss03-02/gaydar-ss03-02.html#work001002',
     u'Гайдар. Судьба барабанщика'],
#    ['grigor_gutt.txt', 4, 'http://ilibrary.ru/text/1333/p.1/index.html', u'Григорович. Гуттаперчевый мальчик'],
#    ['korol_blind.txt', 4, 'http://lib.ru/RUSSLIT/KOROLENKO/slepmuz.txt', u'Короленко. Слепой мальчик'],
    ['ryb_kortik.txt', 4, 'http://lib.rus.ec/b/170890/read', u'Рыбаков. Кортик'],
    ['ryb_bird.txt', 4, 'http://lib.rus.ec/b/145680/read', u'Рыбаков. Бронзовая птица'],
    ['tolst_nikita.txt', 4, 'http://az.lib.ru/t/tolstoj_a_n/text_0040.shtml', u'Толстой. Детство Никиты'],

    ['alisa_advent.txt', 5, 'http://www.rusf.ru/kb/stories/puteshestvie_alisy/text-01.htm',
     u'Кир Булычев. Приключения Алисы'],

    ['text_paust.txt', 6, 'http://paustovskiy.niv.ru/paustovskiy/text/zolotaya-roza/roza_17.htm',
     u'Паустовский. Старик в станционном буфете'],
    ['text_paust2.txt', 6, 'http://paustovskiy.niv.ru/paustovskiy/text/zolotaya-roza/roza_1.htm',
     u'Паустовский. Драгоценная пыль'],
    ['text_avenger.txt', 6, 'http://www.litra.ru/fullwork/get/woid/00051901184773070734/', u'Солоухин. Мститель'],
    ['text_srezal.txt', 6, 'http://www.serann.ru/text/srezal-8707', u'Шукшин. Срезал'],

    ['text_morning.txt', 7, 'http://lib.ru/PROZA/KAZAKOW/r_tihoe_utro.txt', u'Юрий Казаков. Тихое утро'],
    ['text_dvakap.txt', 7, 'http://lib.rus.ec/b/270921/read', u'Вениамин Александрович Каверин. Два капитана.'],

    ['tolst_yun.txt', 8, 'http://ilibrary.ru/text/1334/p.2/index.html', u'Л. Толстой. Юность'],
    ['sab_blad.txt', 8, 'http://www.lib.ru/PRIKL/SABATINI/blood.txt', u'Саббатини. Одиссея капитана Блада'],
    ['koll_stone.txt', 8, 'http://www.lib.ru/DETEKTIWY/KOLLINZ/lunnyjkamen.txt', u'Коллинз. Лунный камень'],
    ['astafiev_soldier.txt', 9, 'http://lib.ru/PROZA/ASTAFIEW/soldat.txt', u'Астафьев. Вслёлый солдат.'],
    ['matrenin_dvor.txt', 9, 'http://www.lib.ru/PROZA/SOLZHENICYN/matren.txt', u'Солженицын. Матрёнин двор.'],
    ['korolenko_deti.txt', 10, 'http://lib.ru/RUSSLIT/KOROLENKO/detipodz.txt', u'Короленко. Дети подземелья'],
    ['zwezda.txt', 10, 'http://lib.ru/PROZA/KAZAKEWICH/zwezda.txt', u'Казакевич. Звезда'],
    ['naveki.txt', 10, 'http://www.lib.ru/PROZA/BAKLANOW/nineteen.txt', u'Бакланов. Навеки - девятнадцатилетние.'],
#    ['kuprin_alesya.txt', 11, 'http://www.kostyor.ru/literature/liter22.html', u'Куприн. Олеся'],
    ['kuprin_braslet.txt', 11, 'http://az.lib.ru/k/kuprin_a_i/text_0170.shtml', u'Куприн. Гранатовый браслет'],
#    ['bunin_udar.txt', 11, 'http://lib.ru/BUNIN/bunin02.txt', u'Бунин. Солнечный удар'],
#    ['bunin_gospodin.txt', 11, 'http://lib.ru/BUNIN/bunin_gospodin.txt', u'Бунин. Господин из Сан-Франциско'],
    ['averchenko_nadkin.txt', 11, 'http://lib.ru/RUSSLIT/AWERCHENKO/averchenko_telegraph.txt', u'Аверченко. '
                                                                                               u'Телеграфист Надькин'],
#    ['platonov_kotlovan.txt', 11, 'http://ilibrary.ru/text/1010/p.1/index.html', u'Платонов. Котлован'],
#    ['platonov_yushka.txt', 11, 'http://ilibrary.ru/text/1192/p.1/index.html', u'Платонов. Юшка'],
#    ['dovlatov_chemodan.txt', 11, 'http://www.lib.ru/DOWLATOW/chemodan.txt', u'Довлатов. Чемодан'],
    ['andreev_shlem.txt', 11, 'http://az.lib.ru/a/andreew_l_n/text_0050.shtml', u'Андреев. Большой шлем'],
#    ['gorki_izergil.txt', 11, 'http://ilibrary.ru/text/486/p.1/index.html', u'Максим Горький. Старуха Изергиль'],
#    ['shukshin_besk.txt', 11, 'http://www.lib.ru/SHUKSHIN/alesha.txt', u'Шукшин. Алеша Бесконвойный'],
    ['astafiev_parun.txt', 11, 'http://lib.ru/PROZA/ASTAFIEW/parunia.txt', u'Астафьев. Паруня'],
    ['rasputin_pozhar.txt', 11, 'http://lib.ru/PROZA/RASPUTIN/pozhar.txt', u'Валентин Распутин. Пожар'],
#    ['rasputin_zhivi.txt', 11, 'http://lib.ru/PROZA/RASPUTIN/rasputin_zhivi.txt', u'Валентин Распутин. Живи и помни'],
    ['bondarev_hot.txt', 11, 'http://militera.lib.ru/prose/russian/bondarev2/index.html', u'Юрий Бондарев. '
                                                                                          u'Горячий снег'],


#    ['text_wiki.txt', 12, 'http://ru.wikipedia.org/wiki/Дорсет', u'Дорсет'],

    ['text_rglichnosti.txt', 15, 'http://www.rg.ru/2013/07/05/lichnosti.html', u'Перейдем на личности'],

    ['text_msterms.txt', 17, 'http://www.microsoft.com/rus/info/copyright/', u'Условия использования '
                                                                             u'на сайте Microsoft'],


    ['text_budget.txt', 17, 'http://kremlin.ru/acts/15786',
     u'Бюджетное послание Президента Российской Федерации о бюджетной политике в 2013–2015 годах'],
    ['text_medvedev.txt', 17, 'http://government.ru/news/2170', u'Заседание Правительства'],
    ['text_arctic.txt', 17, 'http://government.ru/docs/2753',
     u'О разрешениях на осуществление деятельности в Антарктике'],
    ['fks.txt', 17, 'http://base.consultant.ru/cons/cgi/online.cgi?req=doc;base=LAW;n=144624',
     u'Закон о ФКС'],
    ['minec_polozh.txt', 17, 'http://www.economy.gov.ru/minec/about/rukdocmin/index',
     u'Руководящие документы министерства'],
    ['gov_sudeb.txt', 17, 'http://government.ru/activities/2606',
     u'Комиссия Правительства по законопроектной деятельности одобрила с учётом состоявшегося '
     u'обсуждения законопроект «О судебно-экспертной деятельности в Российской Федерации»'],
    ['adm_reg_minpri.txt', 17, 'http://www.mnr.gov.ru/regulatory/detail.php?ID=130938',
     u'«Об утверждении Административного регламента Федеральной службы по надзору в сфере '
     u'природопользования по предоставлению государственной услуги по выдаче разрешений '
     u'на ввоз в Российскую Федерацию или транзит через территорию Российской Федерации ядовитых веществ»'],
    ['gov_bill2.txt', 17, 'http://government.ru/activities/2464',
     u'Комиссия Правительства по законопроектной деятельности одобрила законопроект, '
     u'направленный на повышение эффективности реализации государственной политики и выполнения '
     u'мероприятий в области гражданской обороны'],
    ['gov_bill_film.txt', 17, 'http://government.ru/activities/2412', u'О внесении в Госдуму законопроекта, направленного на сокращение сроков амортизации нематериальных активов в сфере кино и оптимизацию расходов на рекламу фильмов'],
    ['mintrans_news1.txt', 17, 'http://www.mintrans.ru/news/detail.php?ELEMENT_ID=20464', u'5 июля состоялось совместное заседание'],
    ['scrf_concept.txt', 17, 'http://www.scrf.gov.ru/documents/2/25.html', u'Концепция внешней политики Российской Федерации'],
    ['budget_exp.txt', 17, '', u'Доклад Рабочей группы Государственного совета Российской Федерации «О мерах по повышению эффективности бюджетных расходов»'],
    ['kremlin_pens.txt', 17, 'http://kremlin.ru/acts/18933', u'Внесены изменения в закон об обязательном пенсионном страховании'],
    ['government_upk.txt', 17, 'http://government.ru/activities/3379', u'О внесении в Госдуму законопроекта, направленного на совершенствование особого порядка судебного разбирательства'],
]


GRADE_TEXT = {
    1: u'1 - 3-й класс (возраст примерно: 6-8 лет)',
    2: u'1 - 3-й класс (возраст примерно: 6-8 лет)',
    3: u'1 - 3-й класс (возраст примерно: 6-8 лет)',
    4: u'4 - 6-й класс (возраст примерно: 9-11 лет)',
    5: u'4 - 6-й класс (возраст примерно: 9-11 лет)',
    6: u'4 - 6-й класс (возраст примерно: 9-11 лет)',
    7: u'7 - 9-й класс (возраст примерно: 12-14 лет)',
    8: u'7 - 9-й класс (возраст примерно: 12-14 лет)',
    9: u'7 - 9-й класс (возраст примерно: 12-14 лет)',
    10: u'10 - 11-й класс (возраст примерно: 15-16 лет)',
    11: u'10 - 11-й класс (возраст примерно: 15-16 лет)',
    12: u'1 - 3 курсы ВУЗа (возраст примерно: 17-19 лет)',
    13: u'1 - 3 курсы ВУЗа (возраст примерно: 17-19 лет)',
    14: u'1 - 3 курсы ВУЗа (возраст примерно: 17-19 лет)',
    15: u'4 - 6 курсы ВУЗа (возраст примерно: 20-22 лет)',
    16: u'4 - 6 курсы ВУЗа (возраст примерно: 20-22 лет)',
    17: u'4 - 6 курсы ВУЗа (возраст примерно: 20-22 лет)',
}

POST_GRADE_TEXT_18_24 = u'Аспирантура, второе высшее образование, phD'


def calc_SMOG(n_psyl, n_sent):
    """Метрика SMOG для английского языка"""
    n = 1.0430 * sqrt((float(30.0) / n_sent) * n_psyl) + 3.1291
    return n

def calc_Gunning_fog(n_psyl, n_words, n_sent):
    """Метрика Gunning fog для английского языка"""
    n = 0.4 * ((float(n_words)/ n_sent) + 100 * (float(n_psyl) / n_words))
    return n

def calc_Dale_Chale(n_psyl, n_words, n_sent):
    """Метрика Dale Chale для английского языка"""
    n = 0.1579 * (100.0 * n_psyl / n_words) + 0.0496 * (float(n_words) / n_sent)
    return n

def calc_Flesh_Kincaid(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid для английского языка"""
    n = 206.835 - 1.015 * (float(n_words) / n_sent) - 84.6 * (float(n_syllabes) / n_words)
    return n


def calc_Flesh_Kincaid_rus(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid для русского языка"""
    n = 220.755 - 1.315 * (float(n_words) / n_sent) - 50.1 * (float(n_syllabes) / n_words)
    return n

def calc_Flesh_Kincaid_Grade_rus(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid Grade для русского языка"""
#    n = 0.59 * (float(n_words) / n_sent) + 6.2 * (float(n_syllabes) / n_words) - 16.59
    n = 0.49 * (float(n_words) / n_sent) + 7.3 * (float(n_syllabes) / n_words) - 16.59
    return n



def calc_Flesh_Kincaid_Grade_rus_adapted(n_syllabes, n_words, n_sent, X, Y, Z):
    """Метрика Flesh Kincaid Grade для русского языка с параметрами"""
    if n_words == 0 or n_sent == 0: return 0
    n = X * (float(n_words) / n_sent) + Y * (float(n_syllabes) / n_words) - Z
    return n

# Flesh Kinkaid Grade константы. Подробнее http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
FLG_X_GRADE = 0.318
FLG_Y_GRADE = 14.2
FLG_Z_GRADE = 30.5


def calc_Flesh_Kincaid_Grade_rus_flex(n_syllabes, n_words, n_sent):
    """Метрика Flesh Kincaid Grade для русского языка с константными параметрами"""
#    n = 0.59 * (float(n_words) / n_sent) + 6.2 * (float(n_syllabes) / n_words) - 16.59
    if n_words == 0 or n_sent == 0: return 0

    n = FLG_X_GRADE * (float(n_words) / n_sent) + FLG_Y_GRADE * (float(n_syllabes) / n_words) - FLG_Z_GRADE
    return n


# Coleman Liau константы. Подробнее http://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index

CLI_X_GRADE = 0.055
CLI_Y_GRADE = 0.35
CLI_Z_GRADE = 20.33


def calc_Coleman_Liau_index_adapted(n_letters, n_words, n_sent, x, y, z):
    """ Метрика Coleman Liau для русского языка с адаптированными параметрами """
    if n_words == 0: return 0
    n = x * (n_letters * (100.0 / n_words)) - y * (n_sent * (100.0 / n_words)) - z
    return n

def calc_Coleman_Liau_index(n_letters, n_words, n_sent):
    """ Метрика Coleman Liau для русского языка с константными параметрами """
    if n_words == 0: return 0
    n = CLI_X_GRADE * (n_letters * (100.0 / n_words)) - CLI_Y_GRADE * (n_sent * (100.0 / n_words)) - CLI_Z_GRADE
    return n


# Константы SMOG Index http://en.wikipedia.org/wiki/SMOG
SMOG_X_GRADE = 1.1
SMOG_Y_GRADE = 64.6
SMOG_Z_GRADE = 0.05


def calc_SMOG_index(n_psyl, n_sent):
    """Метрика SMOG для русского языка"""
    if n_sent == 0: return 0
    n = SMOG_X_GRADE * sqrt((float(SMOG_Y_GRADE) / n_sent) * n_psyl) + SMOG_Z_GRADE
    return n


def calc_SMOG_index_adapted(n_psyl, n_sent, x, y, z):
    """Метрика SMOG для русского языка адаптированная с коэффициентами"""
    n = x * sqrt((float(y) / n_sent) * n_psyl) + z
    return n

DC_X_GRADE = 0.552
DC_Y_GRADE = 0.273


# def calc_Dale_Chale(n_psyl, n_words, n_sent):
#     """Метрика Dale Chale для английского языка"""
#     if n_words == 0 or n_sent == 0: return 0
#     n = DC_X_GRADE * (100.0 * n_psyl / n_words) + DC_Y_GRADE * (float(n_words) / n_sent)
#     return n


def calc_Dale_Chale_adapted(n_psyl, n_words, n_sent, x, y):
    """Метрика Dale Chale для английского языка"""
    n = x * (100.0 * n_psyl / n_words) + y * (float(n_words) / n_sent)
    return n

ARI_X_GRADE = 6.26
ARI_Y_GRADE = 0.2805
ARI_Z_GRADE = 31.04


def calc_ARI_index_adapted(n_letters, n_words, n_sent, x, y, z):
    """ Метрика Automated Readability Index (ARI) для русского языка с адаптированными параметрами """
    if n_words == 0 or n_sent == 0: return 0
    n = x * (float(n_letters) / n_words) + y * (float(n_words) / n_sent) - z
    return n

def calc_ARI_index(n_letters, n_words, n_sent):
    """ Метрика Automated Readability Index (ARI) для русского языка с константными параметрами """
    if n_words == 0 or n_sent == 0: return 0
    n = ARI_X_GRADE * (float(n_letters) / n_words) + ARI_Y_GRADE * (float(n_words) / n_sent) - ARI_Z_GRADE
    return n


def load_words(filename):
    """Load words from filename"""
    words = []
    f = open(filename, 'r', encoding="utf-8")
    for l in f:
        words.append(l.strip())
    f.close()
    return words

#FAM_WORDS = load_words('1norm50000.txt')

bad_chars = '(){}<>"\'!?,.:;'


def calc_text_metrics(filename, verbose=True):
    """Расчет метрик"""
    f = open(filename, 'r', encoding="utf-8")
    text = f.read()
    f.close()
    return calc_readability_metrics(text, verbose)


# Number of syllabes for long words
COMPLEX_SYL_FACTOR = 4

def calc_readability_metrics(text, verbose=True):
    sentences = 0
    chars = 0
    spaces = 0
    letters = 0
    syllabes = 0
    words = 0
    complex_words = 0
    simple_words = 0
    wsyllabes = {}

    wordStart = False
    for l in text.splitlines():
        chars += len(l)
#        l = l.decode('utf8')
        for ch in l:
            if ch in SENTENCE_SPLITTERS:
                sentences += 1
            if ch in SPACES:
                spaces += 1

        for w in l.split():
            has_syl = False
            wsyl = 0
#            if len(w) > 1: words += 1
            for ch in w:
                if ch in RU_LETTERS:
                    letters += 1
                if ch in RU_VOWELS:
                    syllabes += 1
                    has_syl = True
                    wsyl += 1
            if wsyl > COMPLEX_SYL_FACTOR:
                complex_words += 1
            elif wsyl < COMPLEX_SYL_FACTOR+1 and wsyl > 0:
                simple_words += 1
            if has_syl:
                words += 1
                v = wsyllabes.get(str(wsyl), 0)
                wsyllabes[str(wsyl)] = v + 1
    metrics = {'c_share': float(complex_words) * 100 / words if words > 0 else 0,
               'avg_slen' : float(words) / sentences if sentences > 0 else 0,
               'avg_syl' : float(syllabes) / words if words > 0 else 0,
               'n_syllabes': syllabes,
               'n_words' : words,
               'n_sentences': sentences,
               'n_complex_words': complex_words,
               'n_simple_words' : simple_words,
               'chars': chars,
               'letters' : letters,
               'spaces' : spaces,

               #               'index_fk_rus': calc_Flesh_Kincaid_Grade_rus(syllabes, words, sentences),
               'wsyllabes' : wsyllabes,
    }

    indexes = {
               'index_fk': calc_Flesh_Kincaid_Grade_rus_flex(syllabes, words, sentences),
               'index_cl' : calc_Coleman_Liau_index(letters, words, sentences),
               'index_dc' : calc_Dale_Chale(complex_words, words, sentences),
               'index_SMOG' : calc_SMOG_index(complex_words, sentences),
               'index_ari' : calc_ARI_index(letters, words, sentences),
    }
    indexes.update({"grade_fk": add_grade_text(indexes['index_fk'])})
    indexes.update({"grade_cl": add_grade_text(indexes['index_cl'])})
    indexes.update({"grade_dc": add_grade_text(indexes['index_dc'])})
    indexes.update({"grade_SMOG": add_grade_text(indexes['index_SMOG'])})
    indexes.update({"grade_ari": add_grade_text(indexes['index_ari'])})

    results = {'metrics': metrics, 'indexes' : indexes}
    del text
    return results


def add_grade_text(grade):
    """

    @rtype : basestring
    """
    grade = round(grade)
    print(grade)
    if grade in GRADE_TEXT:
        text =  GRADE_TEXT[grade]
    elif grade > 17:
        text = POST_GRADE_TEXT_18_24
    else:
        text = u'неизвестно (%d)' % (grade)
    return text



def print_metrics(filename, verbose=True):
    """Расчет метрик"""
    metrics = calc_text_metrics(filename, verbose)["metrics"]

    print(f"(Файл - {filename})")
    if verbose:
        print(
            f"- Символов: {metrics['chars']}\n"
            f"- Букв: {metrics['letters']}\n"
            f"- Пробелов: {metrics['spaces']}\n"
            f"- Слов: {metrics['n_words']}\n"
            f"- Сложных слов: {metrics['n_complex_words']}\n"
            f"- Слогов: {metrics['n_syllabes']}\n"
            f"- Предложений: {metrics['n_sentences']}\n"
            f"- Доля сложных слов: {metrics['c_share']}\n"
            f"- Слов: {metrics['n_words']}\n"
            f"- Среднее число слогов на слово: {metrics['avg_syl']}\n"
            f"- Среднее число слов на предложение: {metrics['avg_slen']}\n"
        )
    print('- SMOG: %f' %(calc_SMOG(metrics['n_complex_words'], metrics['n_sentences'])))
    print('- Gunning fog: %f' %(calc_Gunning_fog(metrics['n_complex_words'], metrics['n_words'], metrics['n_sentences'])))
    print('- Dale-Chale: %f' %(calc_Dale_Chale(metrics['n_complex_words'], metrics['n_words'], metrics['n_sentences'])))
    print('- Flesh Kincaid: %f' %(calc_Flesh_Kincaid(metrics['n_syllabes'], metrics['n_words'], metrics['n_sentences'])))
#    print('- Flesh Kincaid (rus): %f' %(calc_Flesh_Kincaid_rus(metrics['n_syllabes'], metrics['n_words'], metrics['n_sentences'])))
    grade = calc_Flesh_Kincaid_Grade_rus(metrics['n_syllabes'], metrics['n_words'], metrics['n_sentences'])
    abs_grade = round(grade)
    print('- Flesh Kincaid Grade (rus): %f' %(grade))
    if abs_grade in GRADE_TEXT:
        text =  GRADE_TEXT[abs_grade]
    elif abs_grade > 17:
        text = POST_GRADE_TEXT_18_24
    else:
        text = u'неизвестно (%d)' % (grade)
    print('- Grade level: %s' % text)


def generate_all_metrics(outfile="metrics.csv"):
    f = open(outfile, 'w')
    fieldnames = ['filename', 'name', 'grade', 'index_fk_rus', 'fk_grade_diff', 'index_cl_rus', 'cl_grade_diff', 'index_dc_rus', 'dc_grade_diff', 'index_SMOG_rus', 'SMOG_grade_diff', 'index_ari_rus', 'ari_grade_diff', 'chars', 'spaces', 'letters', 'n_syllabes', 'n_words', 'n_complex_words', 'n_simple_words', 'n_sentences', 'c_share', 'avg_syl', 'avg_slen', 'wsyllabes']
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    diffs = []
    for text in TEXT_LIST:
        metrics = calc_text_metrics(os.path.join(TEXTSBYGRADE_PATH, f"{text[1]}", f"{text[0]}"))
        print(text[0])
        for k, v in metrics['wsyllabes'].items():
            print("- %s: %d of %d (%f)" %(k, v, metrics['n_words'], float(v) * 100.0 / metrics['n_words']))
        print('- simple words: %d (%f%%)' % (metrics['n_simple_words'], float(metrics['n_simple_words']) * 100.0 / metrics['n_words']))

        metrics['name'] = text[3]
        metrics['filename'] = text[0]
        metrics['grade'] = text[1]
        if metrics['grade'] >= 17 and metrics['index_fk_rus'] >= 17:
            grade_diff = 0
        else:
            grade_diff = metrics['grade'] - metrics['index_fk_rus']
        metrics['fk_grade_diff'] = grade_diff

        if metrics['grade'] >= 17 and metrics['index_cl_rus'] >= 17:
            grade_diff = 0
        else:
            grade_diff = metrics['grade'] - metrics['index_cl_rus']
        metrics['cl_grade_diff'] = grade_diff

        if metrics['grade'] >= 17 and metrics['index_dc_rus'] >= 17:
            grade_diff = 0
        else:
            grade_diff = metrics['grade'] - metrics['index_dc_rus']
        metrics['dc_grade_diff'] = grade_diff

        if metrics['grade'] >= 17 and metrics['index_SMOG_rus'] >= 17:
            grade_diff = 0
        else:
            grade_diff = metrics['grade'] - metrics['index_SMOG_rus']
        metrics['SMOG_grade_diff'] = grade_diff

        if metrics['grade'] >= 17 and metrics['index_ari_rus'] >= 17:
            grade_diff = 0
        else:
            grade_diff = metrics['grade'] - metrics['index_ari_rus']
        metrics['ari_grade_diff'] = grade_diff


        diffs.append(grade_diff)
        for k in metrics.keys():
            metrics[k] = metrics[k].encode('utf8') if type(metrics[k]) == type(u'') else str(metrics[k])
        writer.writerow(metrics)
    avg_diff = mean(diffs)
    diffs.sort()
    print(diffs)
    print(avg_diff)
    f.close()

def print_all_metrics():
    for text in TEXT_LIST:
        print("#", text[3].encode('utf8'))
        print_metrics(os.path.join(TEXTSBYGRADE_PATH, f"{text[1]}", f"{text[0]}"))
        print("----")


def load_metrics():
    allmetrics = []
    for text in TEXT_LIST:
#        if text[1] > 16: continue
        metrics = calc_text_metrics(os.path.join(TEXTSBYGRADE_PATH, f"{text[1]}", f"{text[0]}"))
        metrics['name'] = text[3]
        metrics['filename'] = text[0]
        metrics['grade'] = text[1]
        allmetrics.append(metrics)
    return allmetrics

def calc_diff(allmetrics, func, keys, testvals):
    diffs = []
    failed = False
    for metrics in allmetrics:
        args = []
        for k in keys:
            args.append(metrics[k])
        args.extend(testvals)
        value = func(*args)
        if value < 0:
            failed = True
            break
        if metrics['grade'] >= 17 and value >= 17:
            diffs.append(0)
        else:
            thediff = metrics['grade'] - value
            coeff = 1
            if thediff > 0:
                thediff = coeff * thediff
            diffs.append(abs(thediff))
    if failed:
        return []
    return diffs


COEFF_DIFF_MAX = 1
COEFF_DIFF_MEAN = 1

def calc_hybrid_diff(avg_max, avg_mean, expected_max, expected_mean):
    diff_max = abs(expected_max - avg_max)
    diff_mean = abs(expected_mean - avg_mean)
    return diff_max * COEFF_DIFF_MAX + diff_mean * COEFF_DIFF_MEAN

def adapt_algorithm_2r(func, keys=[], ranges=[], expected_max=3.0, expected_mean=1.1):
    best_diff = [-1, -1, -1]
    best_mark = [0, 0, 0]
    best_diffs = []
    allmetrics = load_metrics()
    if len(ranges) < 2:
      return
    n = 0
    total = 1
    for r in ranges:
        total *= (r[1] - r[0]) / r[2]
        print(r)

    for r1 in arange(*ranges[0]):
        for r2 in arange(*ranges[1]):
            n += 1
            if n % 1000 == 0:
                print('Processing %d of %d' % (n, total), 'values', r1, r2)
            diffs = calc_diff(allmetrics, func, keys, [r1, r2])
#            print diffs

            avg_mean = mean(diffs)
            avg_max = max(diffs)
            avg_hybrid = calc_hybrid_diff(avg_max, avg_mean, expected_max, expected_mean)
            if best_diff[0] != -1:
                if avg_hybrid < best_diff[0]:
                    best_diff = [avg_hybrid, avg_mean, avg_max]
                    best_mark = [r1, r2]
                    print('Best - x: %f, y: %f with hybrid %f, mean %f and max %f' %(r1, r2, avg_hybrid, avg_mean, avg_max))
                    best_alldiffs = diffs
            else:
                best_diff = [avg_hybrid, avg_mean, avg_max]
                best_mark = [r1, r2]
                best_alldiffs = diffs
    print('Best - x: %f, y: %f with value hybrid %f, max %f, mean %f ' %(best_mark[0], best_mark[1], best_diff[0], best_diff[1], best_diff[2]))

def adapt_algorithm_3r(func, keys=[], ranges=[], expected_max=3.0, expected_mean=1.1):
    best_diff = [-1, -1, -1]
    best_mark = [0, 0, 0]
    best_diffs = []
    allmetrics = load_metrics()
    if len(ranges) < 2:
      return
    n = 0
    total = 1
    for r in ranges:
        total *= (r[1] - r[0]) / r[2]
        print(r)

    for r1 in arange(*ranges[0]):
        for r2 in arange(*ranges[1]):
            for r3 in arange(*ranges[2]):
                n += 1
                if n % 1000 == 0:
                    print('Processing %d of %d' % (n, total), 'values', r1, r2, r3)
                diffs = calc_diff(allmetrics, func, keys, [r1, r2, r3])
                if len(diffs) == 0: continue
                avg_mean = mean(diffs)
                avg_max = max(diffs)
                avg_hybrid = calc_hybrid_diff(avg_max, avg_mean, expected_max, expected_mean)
                if best_diff[0] != -1:
                    if avg_hybrid < best_diff[0]:
                        best_diff = [avg_hybrid, avg_mean, avg_max]
                        best_mark = [r1, r2, r3]
                        print('Best - x: %f, y: %f, z: %f with hybrid %f, mean %f and max %f' %(r1, r2, r3, avg_hybrid, avg_mean, avg_max))
                    best_alldiffs = diffs
                else:
                    best_diff = [avg_hybrid, avg_mean, avg_max]
                    best_mark = [r1, r2, r3]
    print(
        f"Best - x: {best_mark[0]}, y:{best_mark[1]}, z: {best_mark[2]} "
        f"with value hybrid {best_diff[0]}, mean {best_diff[1]}, max {best_diff[2]}"
    )


if __name__ == "__main__":
#    generate_all_metrics()
#    adapt_algorithm_2r(calc_Dale_Chale_adapted, ['n_complex_words', 'n_words', 'n_sentences'], ranges=[[0.4, 1.2, 0.001], [0.01, 0.3, 0.001]], expected_max=0, expected_mean=0)
#    adapt_algorithm_3r(calc_ARI_index_adapted, ['letters', 'n_words', 'n_sentences'], ranges=[[6.26, 6.27, 0.001], [0.28, 0.4, 0.0001], [30, 40, 0.01]], expected_max=0, expected_mean=0)
#    adapt_algorithm_3r(calc_SMOG_index_adapted, ['n_complex_words', 'n_sentences'], ranges=[[0.5, 1.5, 0.05], [60, 90, 0.2], [0.001, 5, 0.001]], expected_max=0, expected_mean=0)
#     adapt_algorithm_3r(calc_Flesh_Kincaid_Grade_rus_adapted, ['n_syllabes', 'n_words', 'n_sentences'], ranges=[[0.001, 0.4, 0.001], [4, 20, 0.1], [10, 40, 0.05]], expected_max=0, expected_mean=0)
#    adapt_algorithm_3r(calc_Coleman_Liau_index_adapted, ['letters', 'n_words', 'n_sentences'], ranges=[[0.042, 0.08, 0.001], [0.3, 0.8, 0.01], [10, 30, 0.01]], expected_max=0, expected_mean=0)
#    adapt_ARI_algorithm()
#    adapt_SMOG_algorithm()
#    adapt_DL_algorithm()
#    adapt_FLG_algorithm()
#    adapt_CLI_algorithm()

    print_all_metrics()
