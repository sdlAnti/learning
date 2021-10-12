# Contain all method for reportingp

import smtplib
from config import *
import requests

def send_email(subject, to_addr, body_text):
    BODY = '\r\n'.join((
        f"From: {EMAILLOGIN}@yandex.ru",
        f"To: {to_addr}",
        f"Subject: {subject}",
        "",
        body_text
    ))
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(EMAILLOGIN, EMAILTOKEN)
    server.sendmail(EMAILLOGIN+'@yandex.ru', EMAILSTO, BODY)
    server.quit()


def send_telegram(chat_id, message):
    send_text = 'https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()