import time
import json
import requests
import random
from tls_client import Session
from twocaptcha import TwoCaptcha
from urllib.parse import quote_plus
API_KEY = "CAP-84A565EA65550AF1518A61A2F07079D3"
API_KEY = "CAP-D6F27F6CDE39A17D9370DB2B15482C84" #mine
# TODO: YOUR_PROXY
PROXY = "geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_city-tallahassee"
# PROXY = "us-ca.proxymesh.com:31280"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# SITE_URL_WITH_DATADOME = "https://www.footlocker.com/"
SITE_URL_WITH_DATADOME = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55"


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
def get_captcha_url(url_with_datadome):
    goodheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}]

    session = Session("chrome_120") 
    page_url = url_with_datadome
    proxies = ["u0a8c217b562505b8-zone-custom-region-fr-st-hautsdefrance-session-YIoEDAZjc-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
            "u0a8c217b562505b8-zone-custom-region-id-st-jakarta:u0a8c217b562505b8@43.152.113.55:2333",
            "u0a8c217b562505b8-zone-custom-region-sg:u0a8c217b562505b8@43.152.113.55:2333",
            "u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
            ]
    
    for proxy in proxies:
        time.sleep(3)
        try:
            session.proxies.update({
                "http": f"http://{proxy}",
                "https":f"http://{proxy}",
            })

            while True:
                session.headers = random.choice(goodheaders)
                geo = ""
                print(proxy)
                response = session.get(page_url)
                print(response.text)
                if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
                    if 'dd=' in response.text:
                        dd = response.text.split('dd=')[1]
                        dd = dd.split('</script')[0]
                        dd = json.loads(dd.replace("'", '"'))
                        # breakpoint()
                        cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
                        cid = cid.split(';')[0]
                        try:
                            geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={quote_plus(dd['cid'])}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={quote_plus(page_url)}&s={dd['s']}&e={dd['e']}"
                        except:
                            continue

                        if dd['t'] == "fe":
                            # breakpoint()
                            # # passed.append(str(datetime.datetime.now()))
                            # # breakpoint()
                            # call_capsolver(web_url=page_url, captcha_url=geo, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', proxy="43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-au:u0a8c217b562505b8")
                            return geo
        except Exception as e:
            print(str(e))
            continue

def format_proxy(px: str):
    if '@' not in px:
        sp = px.split(':')
        if len(sp) == 4:
            px = f'{sp[2]}:{sp[3]}@{sp[0]}:{sp[1]}'
    return {"http": f"http://{px}", "https": f"http://{px}"}

def get_page_with_cookie(url, cookie=None):
    headers = HEADERS_TEMPLATE.copy()
    if cookie:
        headers['cookie'] = f"datadome={cookie}"
    try:
        response = requests.get(url, headers=headers, proxies=format_proxy(PROXY), timeout=(20, 20), verify=False)
        print(response.text)
        print(response.status_code)
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def extract_captcha_url(response):
    if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
        if 'dd=' in response.text:
            dd = response.text.split('dd=')[1]
            dd = dd.split('</script')[0]
            dd = json.loads(dd.replace("'", '"'))
            cid = response.headers.get('Set-Cookie').split('datadome=')[1]
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

def call_capsolver(web_url, captcha_url):
    # session = Session("chrome_120")
    data = {
        "clientKey": API_KEY,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": web_url,
            "captchaUrl": captcha_url,
            "userAgent": USER_AGENT,
            "proxy": PROXY
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    breakpoint()
    
    res = requests.post('https://api.capsolver.com/createTask', headers=headers, json=data)
    resp = res.json()
    task_id = resp.get('taskId')
    if not task_id:
        print("create task failed:", res.text)
        return
    while True:
        time.sleep(1)
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
            return cookie
        if status == "failed" or resp.get("errorId"):
            print("failed to solve datadome:", res.text)
            return
        print('solve datadome status:', status)

def two_captcha_solve(website_url, captcha_url):
    headers = {"Content-Type": "application/json","Accept": "application/json",}
    data = {"clientKey": "62948542c9179172367800cc20abfe59", "task": {"type": "DataDomeSliderTask", "websiteURL": website_url, "captchaUrl": captcha_url, "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3", "proxyType":"http", "proxyAddress":"43.152.113.55", "proxyPort": "2333", "proxyLogin":"u0a8c217b562505b8-zone-custom-region-fr-st-hautsdefrance","proxyPassword":"u0a8c217b562505b8"}}
    res = requests.post('https://api.2captcha.com/createTask', headers=headers, json=data)
    resp = res.json()
    task_id = resp.get('taskId')
    data2 = {"clientKey": "62948542c9179172367800cc20abfe59","taskId": task_id}
    while True:
        time.sleep(2)
        res = requests.post('https://api.2captcha.com/getTaskResult', headers=headers, json=data2)
        resp = res.json()
        status = resp.get('status', '')
        if status == "ready":
            cookie = resp['solution']['cookie']
            cookie = cookie.split(';')[0].split('=')[1]
            print("successfully got cookie:", cookie)
            return cookie
        if status == "failed" or resp.get("errorId"):
            print("failed to solve datadome:", res.text)
            return
        print('solve datadome status:', status)

def test_register_page():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="129.0.2792.52", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.59"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'referer': SITE_URL_WITH_DATADOME,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    # response = get_page_with_cookie(SITE_URL_WITH_DATADOME)
    # print("Getting captcha url")
    captcha_url = get_captcha_url(SITE_URL_WITH_DATADOME)
    # proxy = 'u0a8c217b562505b8-zone-custom-region-id-st-jakarta-city-jakarta:u0a8c217b562505b8@43.152.113.55:2333'
    # captcha_url2 = "https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAx9ZfWC4dSdUAtPMgCQ%3D%3D&hash=2211F522B61E269B869FA6EAFFB5E1&cid=Qv2bHoWqN4guL9N866eXQZBtOv2ghSc2ccTE2PdORHVA3Fz2GLyO6KFuu1R0Mg4~NLZDrFGtnYnUBV4LaL8DyQ~5bprOs4BP2kHiyDfVnpgP2koJtIyj3M7Bg7JzX4we&t=fe&referer=https%3A%2F%2Fwww.hermes.com%2Fus%2Fen%2Fproduct%2Flindy-ii-mini-bag-H085956CK8Q%2F&s=13461&e=eb9019a910a8628377f28188371c51a419eafe42ceb1e0559ffdf4abf609d251&dm=cd"
    # headers = {"Content-Type": "application/json","Accept": "application/json",}
    # data = {"clientKey": "62948542c9179172367800cc20abfe59", "task": {"type": "DataDomeSliderTask", "websiteURL": "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55", "captchaUrl": captcha_url, "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3", "proxyType":"http", "proxyAddress":"43.152.113.55", "proxyPort": "2333", "proxyLogin":"u0a8c217b562505b8-zone-custom-region-fr-st-hautsdefrance","proxyPassword":"u0a8c217b562505b8"}}
    # res = requests.post('https://api.2captcha.com/createTask', headers=headers, json=data)
    # resp = res.json()
    # task_id = resp.get('taskId')
    # data2 = {"clientKey": "62948542c9179172367800cc20abfe59","taskId": task_id}
    # res = requests.post('https://api.2captcha.com/getTaskResult', headers=headers, json=data2)
    two_captcha_solve(website_url="https://www.hermes.com/", captcha_url=captcha_url)
    breakpoint()

    # breakpoint()
    # cookieupdate = result['code'].split("=")[1].split(";")[0]
    # if cookieupdate:
    #     headers['cookie'] = f"datadome={cookieupdate}"

    # response = requests.get(SITE_URL_WITH_DATADOME, headers=headers, proxies=format_proxy(proxy), timeout=(20, 20))
    # breakpoint()

    # print(captcha_url)
    # breakpoint()
    
    # if captcha_url2 and 't=bv' not in captcha_url2:
    #     cookie = call_capsolver(SITE_URL_WITH_DATADOME, captcha_url2)
    #     # breakpoint()
    #     if cookie:
    #         get_page_with_cookie(SITE_URL_WITH_DATADOME, cookie)

if __name__ == '__main__':
    test_register_page()