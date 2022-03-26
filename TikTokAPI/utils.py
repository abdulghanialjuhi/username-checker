import requests
import json


def build_get_url(base_url, params, append=False):
    final_url = base_url
    if append:
        final_url += "&"
    else:
        final_url += "?"
    for key, val in params.items():
        final_url += key + "=" + val + "&"
    final_url = final_url[:-1]
    return final_url


def get_req_json(url, params=None, headers=None):
    headers["Host"] = url.split("/")[2]
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)


def python_list2_web_list(data):
    web_list = "[\""
    web_list += '", "'.join(data)
    web_list += "\"]"
    return web_list
