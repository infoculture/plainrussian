Plain Russian Language / Понятный (простой) русский язык.
============

# Зачем всё это нужно
Оценка читаемости текстов необходима для автоматического определения сложности текстов на русском языке.

# Что было сделано
Есть 5 американских алгоритмов оценки читаемости текстов, это:
*  Flesch-Kinkaid - http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
*  Dale-Chale readability formula - http://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula
*  Coleman-Liau index  - http://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index
*  SMOG - http://en.wikipedia.org/wiki/SMOG
*  Automated Readability Index - http://en.wikipedia.org/wiki/Automated_Readability_Index

Были накоплены тексты на русском языке с разметками по уровню чтения, это:
*  тексты для внеклассного чтения;
*  экспертно размеченные взрослые тексты;
*  особо сложные тексты законов;
*  и так далее.

Все алгоритмы были обучены под русский язык - специальным образом каждая формула была подобрана на основе обучающей выборки.
Для всех формул были применены коэффициенты позволяющие применять их к русским текстам.

На базе этих формул был сделан специальный веб-сервис который позволяет передавать ему текст или ссылку и оценивать его на сложность.

# Как работает API

API доступно по ссылке и http://api.plainrussian.ru/api/1.0/ru/measure/
и для его работы ему необходимо передать параметр url (для ссылки) или text (как текст).

Параметр url передается при обращении через GET запрос, пример такого обращения выглядит вот так: 
- http://api.plainrussian.ru/api/1.0/ru/measure/?url=http://minsvyaz.ru/ru/news/index.php?id_4=44264

вот с примером простого текста:
- http://api.plainrussian.ru/api/1.0/ru/measure/?url=http://www.anekdot.ru/id/674877/

или вот:
- http://api.plainrussian.ru/api/1.0/ru/measure/?url=http://www.gosuslugi.ru/pgu/cms/content/isr/view/00000000000/290/309&debug=1

Результат выглядит вот так:

   `     `
    `{`
        `metrics: `
        `{`
            `wsyllabes: `
            `{`
            `1: 94,`
            `2: 116,`
            `3: 140,`
            `4: 87,`
            `5: 139,`
            `6: 45,`
            `7: 18,`
            `8: 4,`
            `15: 1`
            `},`
            `c_share: 32.142857142857146,`
            `chars: 6000,`
            `avg_slen: 46,`
            `spaces: 510,`
            `n_syllabes: 2232,`
            `n_words: 644,`
            `letters: 5170,`
            `n_sentences: 14,`
            `n_complex_words: 207,`
            `n_simple_words: 437,`
            `avg_syl: 3.4658385093167703`
        `},`
        `status: 0,`
        `indexes: `
        `{`
            `grade_SMOG: "Аспирантура, второе высшее образование, phD",`
            `grade_ari: "Аспирантура, второе высшее образование, phD",`
            `index_fk: 33.342906832298134,`
            `grade_cl: "Аспирантура, второе высшее образование, phD",`
            `grade_fk: "Аспирантура, второе высшее образование, phD",`
            `index_cl: 23.062857142857148,`
            `grade_dc: "Аспирантура, второе высшее образование, phD",`
            `index_dc: 30.300857142857147,`
            `index_ari: 32.11796894409938,`
            `index_SMOG: 34.046178356649776`
        `}`
    `}        `

Кроме того, вместо параметра url можно использовать text, чтобы при запросе передавался текст, а не гиперссылка на текст. Вместо GET-запроса имеет смысл использовать POST, чтобы обойти ограничение на размер URI.  
Пример того, как это выглядит в Python с использованием библиотеки requests:

    import requests
    text = "Здесь может быть Ваш текст"
    response = requests.post("http://api.plainrussian.ru/api/1.0/ru/measure/", data={"text":text})
    response.json()

Параметры означают:
## indexes - набор индикаторов читаемости текста:
* grade_SMOG - уровень образования необходимый для понимания текста по формуле SMOG, человеческим языком
* grade_ari - уровень образования необходимый для понимания текста по формуле Automated Readability Index, человеческим языком
* grade_cl - уровень образования необходимый для понимания текста по формуле Coleman-Liau, человеческим языком
* grade_fk - уровень образования необходимый для понимания текста по формуле Flesch-Kinkaid, человеческим языком
* grade_dc - уровень образования необходимый для понимания текста по формуле Dale-Chale, человеческим языком
* index_SMOG - уровень образования необходимый для понимания текста по формуле SMOG, в годах обучения от 1 до бесконечности
* index_ari - уровень образования необходимый для понимания текста по формуле Automated Readability Index, в годах обучения от 1 до бесконечности
* index_cl - уровень образования необходимый для понимания текста по формуле Coleman-Liau, в годах обучения от 1 до бесконечности
* index_fk - уровень образования необходимый для понимания текста по формуле Flesch-Kinkaid, в годах обучения от 1 до бесконечности
* index_dc - уровень образования необходимый для понимания текста по формуле Dale-Chale, в годах обучения от 1 до бесконечности

## metrics - набор расчетных показателей из текста
*   chars - сколько всего знаков тексте
*   spaces - сколько пробелов в тексте
*   letters - сколько букв в тексте
*   n_words - число слов
*   n_sentences - число предложений
*   n_complex_words - число слов с более чем 4-мя слогами
*   n_simple_words - число слов до 4-х слогов включительно
*   avg_slen - среднее число слов на предложение
*   avg_syl - среднее число слогов на предложение
*   c_share - процент сложных слов от общего числа
*   w_syllabes - словарь из значений: число слогов и число слов с таким числом слогов в этом тексте

Если передать параметр debug=1, то также вернется значение текста которое было передано. 

Вот несколько примеров текстов на которых шло обучение.
- Бианки "Лесной дом", 1-й класс - http://api.plainrussian.ru/api/1.0/ru/measure/?url=http://plainrussian.ru/textsbygrade/1/bianki_lesdom.txt
- Астафьев "Солдат", 9-й класс - http://api.plainrussian.ru/api/1.0/ru/measure/?url=http://plainrussian.ru/textsbygrade/9/astafiev_soldier.txt
и так много документов.



* textmetric - библиотека кода для измерения простоты русского языка


Текстовые файлы в textmetric - это специально подобранные тексты с предварительными возрастными пометками. Это позволяет разрабатывать собственные алгоритмы анализа читабельности, простоты, понятности текстов на базе этих метрик.

textmetric/metrics.csv - перечень метрик 
======================

* filename - имя файла в папке textsbygrade
* name - название текста
* grade - год обучения необходимый для понимания текста, экспертная оценка
* index_fk_rus - измерение сложности текста в годах обучения по формуле Flesch-Kinkaid 
* fk_grade_diff - разница в измерении сложности по формуле Flesch-Kinkaid и предустановленной экспертной оценкой
* index_cl_rus - измерение сложности текста в годах обучения по формуле Coleman-Liau
* cl_grade_diff - разница в измерении сложности по формуле Coleman-Liau и предустановленной экспертной оценкой
* index_dc_rus - измерение сложности текста в годах обучения по формуле Dale-Chale
* dc_grade_diff - разница в измерении сложности по формуле Dale-Chale и предустановленной экспертной оценкой
* index_SMOG_rus - измерение сложности текста в годах обучения по формуле SMOG
* SMOG_grade_diff - разница в измерении сложности по формуле SMOG и предустановленной экспертной оценкой
* index_ari_rus - измерение сложности текста в годах обучения по формуле Automatic Readability Index
* ari_grade_diff - разница в измерении сложности по формуле Automatic Readability Index и предустановленной экспертной оценкой
* chars - число знаков в тексте
* spaces - число пробелов
* letters - число букв
* n_syllabes - общее число слогов 
* n_words - общее число слов
* n_complex_words - число сложных слов
* n_simple_words - число простых слов
* n_sentences - число предложений
* c_share - доля сложных слов в процентах
* avg_syl - среднее число слогов на слово
* avg_slen - среднее число слов на слово
* wsyllabes - словарь частоты слов по количеству слогов значений в формате { "число слогов" : "число слов"}
