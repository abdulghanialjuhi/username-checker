import requests
import json
from instagrapi import Client
from TikTokAPI import TikTokAPI
from time import sleep


# -*- coding: utf-8 -*-
def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def decorator(func):
    def restrictions(username, exception, max_name, min_name=1):

        # check english
        if not is_english(username):
            return {'status': False, 'reason': 'اسم المستخدم يجب ان يكون باللغة الإنجليزية فقط',
                    'function': str(func)}
        # check length
        if len(username) > int(max_name) or len(username) < int(min_name):
            return {'status': False, 'reason': f'اسم المستخدم يجب ان يكون بين {min_name} الى {max_name} حرف',
                    'function': str(func)}

        special_characters = "`''' ._`~!@#$%^&*()-+={[}}|\:;\",'<>?/'''`"
        reason = 'اسم المستخد لايجب ان يحتوي على رموز خاصه، بإستثناء'
        exceptions = [' شرطات سفلية (_) ', '، نقاط (.) ', '، شرطات (-) ']

        # check special characters
        for inx, exc in enumerate(exception):
            special_characters = special_characters.replace(exc, '')
            if exc in exceptions[0]:
                reason += exceptions[0]
            elif exc in exceptions[1]:
                reason += exceptions[1]
            elif exc in exceptions[2]:
                reason += exceptions[2]

        if any(c in special_characters for c in username):
            return {'status': False, 'reason': reason, 'function': str(func)}
        return func(username)
    return restrictions


@decorator
def twitter(username):
    x = f'https://api.twitter.com/i/users/username_available.json?username={username}'
    ses = requests.session()
    req = ses.get(x)
    res = json.loads(req.text)
    if res['reason'] == 'available':
        return {'status': True, 'reason': 'متاح', 'function': 'Twitter'}
    return {'status': False, 'reason': 'غير متاح', 'function': 'Twitter'}


@decorator
def instagram(username):
    try:
        cl = Client(json.load(open('logg-file.json')))
        sleep(1)
    except:
        cl = Client()
        cl.login('reactmovie18', 'lykiolhtddfbpsif')
        json.dump(
            cl.get_settings(),
            open('logg-file.json', 'w')
        )
        sleep(1)
    try:
        cl.user_info_by_username_v1(username)
        return {'status': False, 'reason': 'غير متاح', 'function': 'Instagram'}
    except:
        return {'status': True, 'reason': 'متاح', 'function': 'Instagram'}


@decorator
def tiktok(username):
    # cookie = {
    #     "s_v_web_id": "verify_l0f0u4bx_blXz11di_Ttl8_4lxJ_AECH_54jJ0sTp5Ipo",
    #     "ttwid": "1%7CW3IdzTAJUT2VpkXhRx5pFjnr2ErFV8nQEdWFnZVyqAU%7C1646575305%7C46e558aef6073b18ed8f1e952996b7e31b86442c2ed9446718db4731f0a4da07"
    # }
    try:
        api = TikTokAPI()
        user_obj = api.getUserByName(username)
        if user_obj['statusCode'] == 10202:
            return {'status': True, 'reason': 'متاح', 'function': 'Tiktok'}
        else:
            return {'status': False, 'reason': 'غير متاح', 'function': 'Tiktok'}
    except RuntimeError as rn:
        print(rn)
        return {'status': False, 'reason': 'خطأ', 'function': 'Tiktok'}
    
    # with TikTokApi() as api:
    #     try:
    #         user = api.user(username=username)
    #         print(user.as_dict['uniqueId'])
    #         return {'status': True, 'reason': 'متاح', 'function': 'Tiktok'}
    #     except:
    #         return {'status': False, 'reason': 'غير متاح', 'function': 'Tiktok'}


@decorator
def gmail(username):
    api_key = "e95fa7ab-b998-41bc-b020-bf982a73c0fb"
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': f'{username}@gmail.com'},
        headers={'Authorization': f"Bearer {api_key}"})

    status = response.json()['status']

    if status == 'valid':
        return {'status': False, 'reason': 'غير متاح', 'function': 'Hotmail'}
    elif status == "invalid":
        return {'status': True, 'reason': 'متاح', 'function': 'Hotmail'}


@decorator
def outlook(username):
    api_key = "e95fa7ab-b998-41bc-b020-bf982a73c0fb"
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': f'{username}@outlook.com'},
        headers={'Authorization': f"Bearer {api_key}"})

    status = response.json()['status']

    if status == 'valid':
        return {'status': False, 'reason': 'غير متاح', 'function': 'Outlook'}
    elif status == "invalid":
        return {'status': True, 'reason': 'متاح', 'function': 'Outlook'}


@decorator
def hotmail(username):
    api_key = "e95fa7ab-b998-41bc-b020-bf982a73c0fb"
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': f'{username}@hotmail.com'},
        headers={'Authorization': f"Bearer {api_key}"})

    status = response.json()['status']

    if status == 'valid':
        return {'status': False, 'reason': 'غير متاح', 'function': 'Hotmail'}
    elif status == "invalid":
        return {'status': True, 'reason': 'متاح', 'function': 'Hotmail'}


@decorator
def snapchat(username):
    if username[-1] in '_.-':
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
          f"{username}&xsrf_token=PlEcin8s5H600toD4Swngg"

    r = requests.post(url, headers=headers)
    data = r.json()
    status = data.get("reference").get("status_code")

    if status == "OK":
        return {'status': True, 'reason': 'متاح', 'function': 'Snapchat'}

    return {'status': False, 'reason': 'غير متاح', 'function': 'Snapchat'}


@decorator
def reddit(username):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) " \
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.3"
    headers = {"user-agent": ua}
    params = {"user": username}
    request = requests.get('https://www.reddit.com/api/username_available.json', params=params, headers=headers)
    if request.text == 'true':
        return {'status': True, 'reason': 'متاح', 'function': 'reddit'}
    return {'status': False, 'reason': 'غير متاح', 'function': 'reddit'}

