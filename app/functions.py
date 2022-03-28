import requests
import json
from instagrapi import Client
from TikTokAPI import TikTokAPI
from time import sleep
from app.settings import INSTAGRAM_PASSWORD, INSTAGRAM_USERNAME


# -*- coding: utf-8 -*-
def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def decorator(func):
    def restrictions(username, *args):

        # check if english
        if not is_english(username):
            return {'status': False, 'reason': 'اسم المستخدم يجب ان يكون باللغة الإنجليزية فقط',
                    'function': str(func)}

        # check length
        if len(username) > int(args[1]) or len(username) < int(args[2]):
            return {'status': False, 'reason': f'اسم المستخدم يجب ان يكون بين {args[2]} الى {args[1]} حرف',
                    'function': str(func)}

        special_characters = "`''' ._`~!@#$%^&*()-+={[}}|\:;\",'<>?/'''`"
        reason = 'اسم المستخد لايجب ان يحتوي على رموز خاصه، بإستثناء'
        exceptions = [' شرطات سفلية (_) ', '، نقاط (.) ', '، شرطات (-) ']

        # check special characters
        for inx, exc in enumerate(args[0]):
            special_characters = special_characters.replace(exc, '')
            if exc in exceptions[0]:
                reason += exceptions[0]
            elif exc in exceptions[1]:
                reason += exceptions[1]
            elif exc in exceptions[2]:
                reason += exceptions[2]

        if any(c in special_characters for c in username):
            return {'status': False, 'reason': reason, 'function': str(func)}

        return func(username, *args)
    return restrictions


@decorator
def twitter(*args):
    x = f'https://api.twitter.com/i/users/username_available.json?username={args[0]}'
    ses = requests.session()
    req = ses.get(x)
    res = json.loads(req.text)
    if res['reason'] == 'available':
        return {'status': True, 'reason': 'متاح', 'function': 'Twitter'}
    return {'status': False, 'reason': 'غير متاح', 'function': 'Twitter'}


@decorator
def instagram(*args):

    if args[0][-1] in '.':
        return {'status': False, 'reason': 'اسم المستخدم يجب ان لا ينتهي ب نقطة', 'function': 'instagram'}

    try:
        cl = Client(json.load(open('logg-file.json')))
        sleep(1)
    except:
        cl = Client()
        cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        json.dump(cl.get_settings(), open('logg-file.json', 'w'))
        sleep(1)
    try:
        cl.user_info_by_username_v1(args[0])
        return {'status': False, 'reason': 'غير متاح', 'function': 'instagram'}
    except:
        return {'status': True, 'reason': 'متاح', 'function': 'Instagram'}


@decorator
def tiktok(*args):
    cookie = {
        "s_v_web_id": "verify_l0f0u4bx_blXz11di_Ttl8_4lxJ_AECH_54jJ0sTp5Ipo",
        "ttwid": "1%7CW3IdzTAJUT2VpkXhRx5pFjnr2ErFV8nQEdWFnZVyqAU%7C1646575305%7C46e558aef6073b18ed8f1e952996b7e31b86442c2ed9446718db4731f0a4da07"
    }
    api = TikTokAPI(cookie=cookie)
    user_obj = api.getUserByName(args[0])
    if user_obj['statusCode'] == 10202:
        return {'status': True, 'reason': 'متاح', 'function': 'Tiktok'}
    else:
        return {'status': False, 'reason': 'غير متاح', 'function': 'Tiktok'}


@decorator
def mail(*args):

    if args[0][-1] in '_.-':
        return {'status': False, 'reason': 'اسم المستخدم يجب ان لا ينتهي برمز', 'function': args[4]}

    api_key = "e95fa7ab-b998-41bc-b020-bf982a73c0fb"
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': f'{args[0]}@{args[4]}.com'},
        headers={'Authorization': f"Bearer {api_key}"})

    status = response.json()['status']

    if status == 'valid':
        return {'status': False, 'reason': 'غير متاح', 'function': args[4]}

    return {'status': True, 'reason': 'متاح', 'function': args[4]}


@decorator
def snapchat(*args):
    if args[0][-1] in '_.-':
        return {'status': False, 'reason': 'اسم المستخدم يجب ان لا ينتهي برمز', 'function': 'Snapchat'}

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }

    url = f"https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username=" \
          f"{args[0]}&xsrf_token=PlEcin8s5H600toD4Swngg"

    r = requests.post(url, headers=headers)
    data = r.json()
    status = data.get("reference").get("status_code")

    if status == "OK":
        return {'status': True, 'reason': 'متاح', 'function': 'Snapchat'}

    return {'status': False, 'reason': 'غير متاح', 'function': 'Snapchat'}


@decorator
def reddit(*args):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) " \
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.3"
    headers = {"user-agent": ua}
    params = {"user": args[0]}
    request = requests.get('https://www.reddit.com/api/username_available.json', params=params, headers=headers)
    if request.text == 'true':
        return {'status': True, 'reason': 'متاح', 'function': 'reddit'}
    return {'status': False, 'reason': 'غير متاح', 'function': 'reddit'}
