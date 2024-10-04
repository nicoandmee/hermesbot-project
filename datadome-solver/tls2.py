from tls_client import Session
import json
from browserforge.fingerprints import Screen, FingerprintGenerator
from browserforge.headers import Browser, HeaderGenerator
import time
import random
import datetime
import requests
API_KEY = "CAP-84A565EA65550AF1518A61A2F07079D3"

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

def call_capsolver(web_url, captcha_url, user_agent, proxy):
    data = {
        "clientKey": API_KEY,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": web_url,
            "captchaUrl": captcha_url,
            "userAgent": user_agent,
            "proxy": proxy
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    res = requests.post('https://api.capsolver.com/createTask', headers=headers, json=data)
    resp = res.json()
    task_id = resp.get('taskId')
    breakpoint()
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


# def get_captcha_url():
#     goodheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
#         {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}]

#     session = Session("chrome_120") 
#     page_url = 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'
#     proxies = ["u0a8c217b562505b8-zone-custom-region-cn-st-shanghai:u0a8c217b562505b8@43.159.28.126:2333",
#             "u0a8c217b562505b8-zone-custom-region-id-st-jakarta:u0a8c217b562505b8@43.152.113.55:2333",
#             "u0a8c217b562505b8-zone-custom-region-sg:u0a8c217b562505b8@43.152.113.55:2333",
#             "u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
#             ]
    
#     for proxy in proxies:
#         time.sleep(3)
#         try:
#             session.proxies.update({
#                 "http": f"http://{proxy}",
#                 "https":f"http://{proxy}",
#             })

#             while True:
#                 session.headers = random.choice(goodheaders)
#                 geo = ""
#                 print(proxy)
#                 response = session.get(page_url)
#                 print(response.text)
#                 if response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
#                     if 'dd=' in response.text:
#                         dd = response.text.split('dd=')[1]
#                         dd = dd.split('</script')[0]
#                         dd = json.loads(dd.replace("'", '"'))
#                         cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
#                         cid = cid.split(';')[0]
#                         try:
#                             geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={dd['cid']}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={page_url}&s={dd['s']}&e={dd['e']}"
#                         except:
#                             continue

#                         if dd['t'] == "fe":
#                             # # passed.append(str(datetime.datetime.now()))
#                             # # breakpoint()
#                             # call_capsolver(web_url=page_url, captcha_url=geo, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', proxy="43.152.113.55:2333:u0a8c217b562505b8-zone-custom-region-au:u0a8c217b562505b8")
#                             return geo
#         except Exception as e:
#             print(str(e))
#             continue



if __name__ == '__main__':
    geo = get_captcha_url( 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55')
    print(geo)