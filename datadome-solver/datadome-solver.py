import time
import json
import requests
from browserforge.fingerprints import Screen, FingerprintGenerator
from browserforge.headers import Browser
import random
from tls_client import Session

API_KEY = "CAP-84A565EA65550AF1518A61A2F07079D3"
# TODO: YOUR_PROXY
PROXY = "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10004"
# PROXY = "scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181"
PROXIES = [
"u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
"u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
"u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
"u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
"u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",

]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
SITE_URL_WITH_DATADOME = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/"
USER_AGENTS=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',]

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
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga_Y862HCHCQ7=GS1.1.1727359836.3.1.1727360670.0.0.0; __cf_bm=DxTH36bRUxxWS63mEFJ.gNXCNWLjDQux3Pd8.mGmVK8-1727386101-1.0.1.1-yVyh1gu0DKvRglrmMwoQltFpBMATxRkm1cWzCM03V7nHcFBVWdKQ1rvrPgpLNEWWkdhOb9YkUh3tBzYUjV0NoQ; datadome=_RPoxQVAsOaL0nnCyCiyURVMJt1J5NCMUDgtDwm3wYPXF2qko1aupyuSnuq881MqhdPq2hI2vexPbvUJ9BNKfV4HH~xE~ndypTI2GQ3doa9JLqTdZknYHRUSP9QoPL2o',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def get_captcha_url():
    goodheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}]

    session = Session("chrome_120") 
    page_url = 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'
    proxies = ["u0a8c217b562505b8-zone-custom-region-cn-st-shanghai:u0a8c217b562505b8@43.159.28.126:2333",
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
                        cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
                        cid = cid.split(';')[0]
                        try:
                            geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={dd['cid']}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={page_url}&s={dd['s']}&e={dd['e']}"
                        except:
                            continue

                        if dd['t'] == "fe":
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

def get_page_with_cookie(url, cookie=None, headers=None, proxy=None):
    
    print(proxy)
    # headers = HEADERS_TEMPLATE.copy()

    if cookie:
        headers['cookie'] = f"datadome={cookie}"
    try:
        # breakpoint()
        response = requests.get(url, headers=headers, proxies=format_proxy(proxy), timeout=(20, 20))
        # print(response.text)
        
        print(response.status_code)
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def extract_captcha_url(response):
    if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
        # breakpoint()
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

def call_capsolver(web_url, captcha_url):
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
    res = requests.post('https://api.capsolver.com/createTask', headers=headers, json=data, verify=False)
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
        res = requests.post('https://api.capsolver.com/getTaskResult', headers=headers, json=data, verify=False)
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
    screen = Screen(
        min_width=1280, max_width=5120, min_height=720, max_height=2880
    )
    browsers = [
        Browser(name='chrome', min_version=120, max_version=129),
    ]
    xheaders = FingerprintGenerator(
                browser='chrome', os='windows',
                # os=("windows", "macos", "linux"),
                device="desktop",
                locale=("zh-CN", "en"),
                screen=screen,
                http_version=2,
                strict=True,
                mock_webrtc=True,
            )
    temps = xheaders.generate()
    # breakpoint()
    newheaders = {
                "Content-type": "application/x-www-form-urlencoded",
                # "Host": "api-js.datadome.co",
                "Origin": SITE_URL_WITH_DATADOME,
                "Referer": SITE_URL_WITH_DATADOME,
                "Accept-Encoding": temps.headers.get("Accept-Encoding"),
                "Accept-Language": temps.headers.get("Accept-Language"),
                "Sec-Ch-Ua": temps.headers.get("sec-ch-ua"),
                "Sec-Ch-Ua-Mobile": temps.headers.get("sec-ch-ua-mobile"),
                "Sec-Ch-Ua-Platform": temps.headers.get("sec-ch-ua-platform"),
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": temps.headers.get("User-Agent"),
                "Upgrade-Insecure-Requests": temps.headers.get(
                    "Upgrade-Insecure-Requests"
                ),
            }
    
    
    for idx, _ in enumerate(PROXIES):

        try:
            # headers['user-agent'] = USER_AGENTS[idx]
            # response = get_page_with_cookie(SITE_URL_WITH_DATADOME, headers=newheaders, proxy=PROXIES[idx])
            # print("Getting captcha url")
            captcha_url = get_captcha_url()
            time.sleep(2)    
        # breakpoint()
            print(captcha_url)
            if captcha_url and 't=bv' not in captcha_url:
                breakpoint()
                cookie = call_capsolver(SITE_URL_WITH_DATADOME, captcha_url)
                if cookie:
                    get_page_with_cookie(SITE_URL_WITH_DATADOME, cookie)
        except:
            continue    
if __name__ == '__main__':
    test_register_page()
