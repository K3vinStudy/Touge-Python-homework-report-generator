# name: 使用Cookie获取网页内容
# 作者：K3vin
# version：1.1.0
import http.cookiejar
import requests

session = requests.Session()

def get_json_withCookie(target_url):
    # set cookie
    cookie_filename = 'cookie.txt'
    cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie_aff.load(cookie_filename,ignore_discard=True,ignore_expires=True)
    session.cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(cookie_aff))
    respjson = session.get(target_url).json()
    return respjson