# Contains all methods for checking page

from bs4 import BeautifulSoup
import lxml
import requests
import datetime
from config import *
import whois
import idna


def checkStatus(testPage):
    punyPage = ''
    if testPage.startswith('xn--'):
        punyPage = idna.decode(testPage)
        print(punyPage)
    try:
        if testPage == '':
            return 999
        if not testPage.startswith('http'):
            testPage = 'http://'+testPage
        req = requests.get(testPage, HEADERS)


    except:
        return 'Error'
    #     Ретун тут это плохо и тупо нужно подумать о другом.

    # If whois expressed then send false else true
    ex_date_status = 'OK'
    if not punyPage.endswith('.рус'):
       # try:
        if punyPage:
            who = whois.whois(punyPage)
        else:
            who = whois.whois(testPage)

        if isinstance(who.expiration_date, list):
            ex_date_tmp = who.expiration_date[0]
        else:
            ex_date_tmp = who.expiration_date
        print('exdate' , ex_date_tmp)
        if (ex_date_tmp < datetime.datetime.now()):
            ex_date_status = 'Expressed'
        else:
            ex_date_status = 'OK'
        if not ex_date_status:
            print('hui tebe')
            ex_date_status = 'PISKA'
       # except:
       #      ex_date_status = 'Check failed'


    print(str(datetime.datetime.now()) + ' Checking page ' + testPage + '. Return code: ' + str(req.status_code))
    with open('log.txt', 'a') as file:
        file.write(
            str(datetime.datetime.now()) + ' Checking page ' + testPage + '. Return code: ' + str(type(req.status_code)) +
            str(req.status_code) + ' compare with 200' + str(req.status_code == 200) + '\n')
    return req.status_code, ex_date_status

