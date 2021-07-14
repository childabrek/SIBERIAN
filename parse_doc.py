import requests


def one_use():

    url_0 = 'https://docs.google.com/document/d/1ehCvMVRWZJlb04ztIHsph-3RrREOlsPfHfqRlx297fo/export?format=txt'
    # binary open install and save
    with open('one_use.txt', 'wb') as first:
        ufr_0 = requests.get(url_0)
        first.write(ufr_0.content)  # записываем содержимое в файл; как видите - content запроса

    # read file before install
    with open('one_use.txt', 'r', encoding='utf-8') as second:
        # some ugly code
        answer = second.read()
        answer = answer.replace('﻿horizontal line \n\n', '')
        while '\n\n\n' in answer:
            answer = answer.replace('\n\n\n', '\n\n')

    # save all our shit
    with open('one_use.txt', 'w', encoding='utf-8') as third:
        third.write(answer)


def hardware():
    url = 'https://docs.google.com/document/d/1ikzohprimODR4ch-jdmA0hTdBvqG-PSczKGQ0kAPqjQ/export?format=txt'

    with open('hardware.txt', 'wb') as first:
        ufr = requests.get(url)
        first.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса

    # read file before install
    with open('hardware.txt', 'r', encoding='utf-8') as second:
        # some ugly code
        answer = second.read()
        answer = answer.replace('﻿horizontal line \n\n', '').replace('_', '')
        answer = answer.replace('Железо', '').replace('\n\n\n', '', 1)
        # print(answer)
        while '\n\n\n' in answer:
            answer = answer.replace('\n\n\n', '\n\n')

    with open('hardware.txt', 'w', encoding='utf-8') as third:
        print(answer)
        third.write(answer)


def liquids_standart():
    url = 'https://docs.google.com/document/d/1JNB-hx19OfUGwV0g5oR3-Ng8G6fnk9cgs3Q35va9rYU/export?format=txt'

    with open('liquids_standart.txt', 'wb') as first:
        ufr = requests.get(url)
        first.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса

    # read file before install
    with open('liquids_standart.txt', 'r', encoding='utf-8') as second:
        # some ugly code
        answer = second.read()
        answer = answer.replace('﻿horizontal line \n\n', '').replace('_', '')
        answer = answer.replace('Описание вкусов :\n', '')
        # print(answer)
        while '\n\n\n' in answer:
            answer = answer.replace('\n\n\n', '\n\n')

    with open('liquids_standart.txt', 'w', encoding='utf-8') as third:
        print(answer)
        print(len(answer))
        third.write(answer)


# def liquids_salt():
#     url = 'https://docs.google.com/document/d/1QGe5vdug10jfwSuHAy3-qiJPEAV8A8lGgT5nLGTMNmg/export?format=txt'
#
#     with open('liquids_salt.txt', 'wb') as first:
#         ufr = requests.get(url)
#         first.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса
#
#     # read file before install
#     with open('liquids_salt.txt', 'r', encoding='utf-8') as second:
#         # some ugly code
#         answer = second.read()
#         answer = answer.replace('﻿horizontal line \n\n', '').replace('_', '')
#         answer = answer.replace('Актуальный прайс \n\n', '').replace('Описание вкусов', '')
#         answer = answer.replace(' :\n', '').replace(':\n', '').replace(': \n', '')
#         # print(answer)
#         while '\n\n\n' in answer:
#             answer = answer.replace('\n\n\n', '\n\n')
#
#     with open('liquids_salt.txt', 'w', encoding='utf-8') as third:
#         print(answer)
#         print(len(answer))
#         third.write(answer)

# one_use()
# hardware()
# liquids_standart()