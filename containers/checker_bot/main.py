from config import *
from checkpage import *
from reporting import *
import datetime
import json
from time import sleep


def run_test():
    # Reading all sites to check
    urls = []
    tech_info = {}
    with open('pages_for_check.txt', 'r') as file:
        for el in file:
            urls.append(el.strip())

    # Collecting status codes
    message = f"Start: {datetime.datetime.now()} \n"
    statusForSend = False

    for url in urls:

        status, ex_date = checkStatus(url)
        if status != 200:
            statusForSend = True
            message = message + f'Failed: http://{url}/. Status: {status} \n'
        # if domain have 2 rangs run check for domain expression date
        if url.count('.') == 1:
            if ex_date != 'OK':
                statusForSend = True
                if url.startswith('xn--'):
                    url4msg = idna.decode(url)
                else:
                    url4msg = url
                message = message + f'Failed: Expression date of domain http://{url4msg}/ - expressed. Status: {ex_date} \n'

    message = message + f'End: {datetime.datetime.now()} \n '
    message.encode('utf-8')
    print(message)

    # try:
    #     if statusForSend:
    #         send_email('reporting', 'anosovsrg@gmail.com', message)
    # except:
    #     print('Failed sending email')

    # writting status
    tech_info['last_check'] = str(datetime.datetime.now())
    tech_info['message'] = message

    message = [message[i:i+3000] for i in range(0, len(message), 3000)]

    try:
        if statusForSend:
            for el in TELEGRAM_CHAT_IDS:
                for msg in message:
                    msg = "```\n" + msg + "```"
                    send_telegram(el, msg)
                    sleep(0.3)
        else:
            print('0 errors')
    except:
        print('Failed with sending telegram message')



    with open('lastCheck.json', 'w') as file:
        json.dump(tech_info, file)


run_test()
