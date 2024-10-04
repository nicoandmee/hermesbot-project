import time
import json
import requests
from tls_client import Session as TlsSession
import random
from urllib.parse import quote_plus


API_KEY = "CAP-D6F27F6CDE39A17D9370DB2B15482C84"
# TODO: YOUR_PROXY
PROXY = "u0a8c217b562505b8-zone-custom-region-fr-st-hautsdefrance:u0a8c217b562505b8@43.152.113.55:2333"
proxytasks = [
    "gate.smartproxy.com:10006:spm9mlk9ik:3TlhzhsLf~D7g60Pyj"
]
proxypools = [
    # "gate.smartproxy.com:10002:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",


"gate.smartproxy.com:10001:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10002:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10003:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10004:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10005:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10006:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10007:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10008:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10009:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"gate.smartproxy.com:10010:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-1OLMyn6Lh-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-SiitxPohU-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-AjBuDKCDy-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-r9F7scmVe-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-TWEnM0xqb-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-En0dpJMLb-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-HH3vLJDso-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-kS5YZxlza-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-1vROp4eGQ-sessTime-10:u0a8c217b562505b8",
"43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-id-session-i2PVev7T3-sessTime-10:u0a8c217b562505b8",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-kBOD6dAD_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-HC4kWv9W_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-zolWwKq0_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-JNoRMVhZ_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-hw4xIsUm_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-GKgKVw2Z_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-UOKdVfgp_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-HETOfDqp_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-JOyJkiDV_lifetime-10m",
"geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_session-1gKfrW9R_lifetime-10m",

]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
SITE_URL_WITH_DATADOME = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/"

HEADERS_TEMPLATE = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,en-US;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.200", "Chromium";v="119.0.6045.200", "Not?A_Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': USER_AGENT,
    'referer': SITE_URL_WITH_DATADOME  
}
acceptedheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}]

def format_proxy(px: str):
    if '@' not in px:
        sp = px.split(':')
        if len(sp) == 4:
            px = f'{sp[2]}:{sp[3]}@{sp[0]}:{sp[1]}'
    return {"http": f"http://{px}", "https": f"http://{px}"}

def get_page_with_cookie(url, cookie=None):
    session = TlsSession("chrome_120") 
    session.proxies.update({
        "http": f"http://{PROXY}",
        "https":f"http://{PROXY}",
    })

    # headers = HEADERS_TEMPLATE.copy()
    headers = random.choice(acceptedheaders)
    headers['Origin'] = url
    headers['Referer'] = url
    session.headers.update(headers)
    # breakpoint()
    if cookie:
        headers['cookie'] = f"datadome={cookie}"
    try:
        response = session.get(url)
        print(response.text)
        print(response.status_code)
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_captcha_url(url):
    session = TlsSession("chrome_120") 
    url_with_datadome = url
    proxy = random.choice(proxypools)
    proxysplit = proxy.split(":")
    proxyhttp=f"{proxysplit[-2]}:{proxysplit[-1]}@{proxysplit[0]}:{proxysplit[1]}"
    # breakpoint()
    session.proxies.update({
        "http": f"http://{proxyhttp}",
        "https":f"http://{proxyhttp}",
    })
    geo = ""
    while True:
        try:
            headerchoice = HEADERS_TEMPLATE.copy()
            headerchoice['origin'] = url_with_datadome
            headerchoice['referer'] = url_with_datadome
            session.headers.update(headerchoice)
            # breakpoint()
            geo = ""
            print(proxy)
            response = session.get(url_with_datadome)
            print(response.text)
            # breakpoint()
            if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
                if 'dd=' in response.text:
                    dd = response.text.split('dd=')[1]
                    dd = dd.split('</script')[0]
                    dd = json.loads(dd.replace("'", '"'))
                    # breakpoint()
                    cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
                    cid = cid.split(';')[0]
                    geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={quote_plus(dd['cid'])}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={quote_plus(url_with_datadome)}&s={dd['s']}&e={dd['e']}"
                    if dd['t'] == "fe":
                        # breakpoint()
                        # return (geo, cid)
                        while True:
                            proxy = random.choice(proxypools)
                            cookie = call_capsolver(web_url=url_with_datadome, captcha_url=geo, proxy=proxy)
                            
                    else:
                        continue
                    return ""
                else:
                    print("No dd")
                    continue
        except Exception as e:
            print("error from func_captcha_url:", str(e))
            continue

    

def extract_captcha_url(response):
    if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
        if 'dd=' in response.text:
            dd = response.text.split('dd=')[1]
            dd = dd.split('</script')[0]
            dd = json.loads(dd.replace("'", '"'))
            cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
            cid = cid.split(';')[0]
            return f"https://geo.captcha-delivery.com/captcha/?initialCid={dd['cid']}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={SITE_URL_WITH_DATADOME}&s={dd['s']}&e={dd['e']}"
        else:
            possible_paths = ["/captcha/", "/interstitial/"]
            for path in possible_paths:
                start_index = response.text.find(f"https://geo.captcha-delivery.com{path}")
                if start_index != -1:
                    end_index = response.text.find('"', start_index)
                    return response.text[start_index:end_index]
    return "Not DataDome Captcha / Challenge found"

def call_capsolver(web_url, captcha_url, proxy):
    while True:
        # socks5://user-spm9mlk9ik-session-1:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:7000
        data = {
            "clientKey": API_KEY,
            "task": {
                "type": 'DatadomeSliderTask',
                "websiteURL": web_url,
                "captchaUrl": captcha_url,
                "userAgent": USER_AGENT,
                # "proxy": proxy
                "proxyType": "socks5",
                "proxyAddress": "gate.smartproxy.com",
                "proxyPort": 7000,
                "proxyLogin": "user-spm9mlk9ik-session-1",
                "proxyPassword": "3TlhzhsLf~D7g60Pyj",     
            }
        }
        # breakpoint()
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        res = requests.post('https://api.capsolver.com/createTask', headers=headers, json=data)
        resp = res.json()
        task_id = resp.get('taskId')
        if not task_id:
            print("create task failed:", res.text)
            continue
        time.sleep(5)
        while True:
            # time.sleep(1)
            data = {
                "clientKey": API_KEY,
                "taskId": task_id
            }
            res = requests.post('https://api.capsolver.com/getTaskResult', headers=headers, json=data)
            resp = res.json()
            status = resp.get('status', '')
            if status == "ready":
                cookie = resp['solution']['cookie']
                cookie = cookie.split(';')[0].split('=')[1]
                print("successfully got cookie:", cookie)
                breakpoint()
                # return cookie
            if status == "failed" or resp.get("errorId"):
                print("failed to solve datadome:", res.text)
                break
            print('solve datadome status:', status)

def test_register_page():
    while True:
        response = get_captcha_url(SITE_URL_WITH_DATADOME)
        print("Getting captcha url")
        captcha_url = extract_captcha_url(response)
        print(captcha_url)
        if 't=fe' in captcha_url:
            break
    if captcha_url and 't=bv' not in captcha_url:
        cookie = call_capsolver(SITE_URL_WITH_DATADOME, captcha_url)
        if cookie:
            get_page_with_cookie(SITE_URL_WITH_DATADOME, cookie)

if __name__ == '__main__':
    test_register_page()