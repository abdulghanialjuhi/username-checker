import string
import random
import urllib.parse
from .utils import  build_get_url, get_req_json
from .tiktok_browser import TikTokBrowser


class TikTokAPI(object):

    def __init__(self, cookie=None, language='en', browser_lang="en-US", timezone="Asia/Kolkata", region='IN'):
        self.base_url = "https://t.tiktok.com/api"
        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"

        if cookie is None:
            cookie = {}
        self.verifyFp = cookie.get("s_v_web_id", "verify_kjf974fd_y7bupmR0_3uRm_43kF_Awde_8K95qt0GcpBk")
        self.tt_webid = cookie.get("tt_webid", "6913027209393473025")

        self.headers = {
            'Host': 't.tiktok.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Referer': 'https://www.tiktok.com/',
            'Cookie': 'tt_webid_v2={}; tt_webid={}'.format(self.tt_webid, self.tt_webid)
        }
        self.language = language
        self.browser_lang = browser_lang
        self.timezone = timezone
        self.region = region

        self.default_params = {
            "aid": "1988",
            "app_name": "tiktok_web",
            "device_platform": "web",
            "referer": "",
            "user_agent": urllib.parse.quote_plus(self.user_agent),
            "cookie_enabled": "true",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": self.browser_lang,
            "browser_platform": "Linux+x86_64",
            "browser_name": "Mozilla",
            "browser_version": "5.0+(X11)",
            "browser_online": "true",
            "timezone_name": self.timezone,
            # "page_referer": "https://www.tiktok.com/foryou?lang=en",
            "priority_region": self.region,

            "appId": "1180",
            "region": self.region,
            "appType": "t",

            "isAndroid": "false",
            "isMobile": "false",
            "isIOS": "false",
            "OS": "linux",
            "tt-web-region": self.region,

            "language": self.language,
            "verifyFp": self.verifyFp
        }
        self.signature_key = "_signature"
        self.did_key = "did"
        self.tiktok_browser = TikTokBrowser(self.user_agent)

    def send_get_request(self, url, params, extra_headers=None):
        url = build_get_url(url, params)
        did = ''.join(random.choice(string.digits) for num in range(19))
        url = build_get_url(url, {self.did_key: did}, append=True)
        signature = self.tiktok_browser.fetch_auth_params(url, language=self.language)
        url = build_get_url(url, {self.signature_key: signature}, append=True)
        if extra_headers is None:
            headers = self.headers
        else:
            headers = {}
            for key, val in extra_headers.items():
                headers[key] = val
            for key, val in self.headers.items():
                headers[key] = val
        data = get_req_json(url, params=None, headers=self.headers)
        return data

    def getUserByName(self, user_name):
        url = "https://t.tiktok.com/node/share/user/@" + user_name
        params = {
            "uniqueId": user_name,
            "validUniqueId": user_name,
        }
        for key, val in self.default_params.items():
            params[key] = val
        return self.send_get_request(url, params)
