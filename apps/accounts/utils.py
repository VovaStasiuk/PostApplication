import requests
from os import environ

HUNTER_API_KEY = environ.get('HUNTER_API_KEY')
CLEARBIT_API_KEY = environ.get('CLEARBIT_API_KEY')
CLEARBIT_SECRET_KEY = environ.get('CLEARBIT_SECRET_KEY')


def email_verification(email):
    try:
        if HUNTER_API_KEY is None:
            return True
        res = requests.get(f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={HUNTER_API_KEY}').json()
        if res['data']['result'] == "undeliverable":
            return False
        return True
    except:
        return True


def additional_info(email):
    try:
        option = {
            'auth': (CLEARBIT_API_KEY, CLEARBIT_SECRET_KEY)
        }
        res = requests.get('https://person.clearbit.com/v2/combined/find?email=account@coinswapy.com', **option)
        if res.status_code == 200:

            return res.json()['person']
        return {}
    except:
        pass
