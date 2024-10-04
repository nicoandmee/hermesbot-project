import time
import json
import requests
import random
from tls_client import Session as TlsSession
from twocaptcha import TwoCaptcha
from urllib.parse import quote_plus
from requests import Session
# TODO: YOUR_PROXY
PROXY = "geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_city-tallahassee"
# PROXY = "us-ca.proxymesh.com:31280"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# SITE_URL_WITH_DATADOME = "https://www.footlocker.com/"
SITE_URL_WITH_DATADOME = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55"
API_KEY ="d6438f93a291d130f08e1721d4ac1fdf"


acceptedheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': "", 'Referer': ""}, 
    {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': "", 'Referer': ""}]

productheaders = {
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
    # 'referer': "",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
proxypools = [
        "u0a8c217b562505b8-zone-custom-region-ae-session-6qFzStsfs-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-frQNf3QYI-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-WA24e6vnZ-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-ASHoNxvGG-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-3unEZbLXJ-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-sbAZfpyvF-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-7EzbeW0Sf-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-vWV7BxmZL-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-ekHRhkCF7-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
        "u0a8c217b562505b8-zone-custom-region-ae-session-wlfsd1cCe-sessTime-10:u0a8c217b562505b8@43.152.113.55:2333",
]


def capmonster_solver(website_url, captcha_url, cid):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "clientKey": "d6438f93a291d130f08e1721d4ac1fdf",
        "task": {
            "type": "CustomTask",
            "class": "DataDome",
            "websiteURL": website_url,
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "metadata": {
                # "htmlPageBase64": "PGh0bWw+PGhlYWQ+PHRpdGxlPmJs...PC9odG1sPg==",
                "captchaUrl": captcha_url,
                "datadomeCookie": f"datadome={cid}"
            }
        }
    }
    res = requests.post('https://api.capmonster.cloud/createTask', headers=headers, json=data)
    resp = res.json()
    task_id = resp.get('taskId')
    data2 = {"clientKey": "d6438f93a291d130f08e1721d4ac1fdf","taskId": task_id}
    while True:
        time.sleep(2)
        res = requests.post('https://api.capmonster.cloud/getTaskResult', headers=headers, json=data2)
        resp = res.json()
        status = resp.get('status', '')
        if status == "ready":
            # breakpoint()
            cookie = resp['solution']['domains']['hermes.com']['cookies']['datadome']
            # cookie = cookie.split(';')[0].split('=')[1]
            print("successfully got cookie:", cookie)
            return cookie
        if status == "failed" or resp.get("errorId"):
            print("failed to solve datadome:", res.text)
            return
        print('solve datadome status:', status)

        # breakpoint()

def get_captcha_url(url_with_datadome, proxyidx=0):
    goodheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': url_with_datadome, 'Referer': url_with_datadome}, 
        {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': url_with_datadome, 'Referer': url_with_datadome}]

    session = Session("chrome_120") 
    page_url = url_with_datadome
    
    proxies = [
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10001",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10002",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10003",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10004",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10005",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10006",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10007",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10008",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10009",
        "spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10010",
    ]
    print(url_with_datadome)
    first = True
    while True:
        for idx, proxy in enumerate(proxies):
            if first:
                if idx != proxyidx:
                    continue
                else:
                    first = False
            try:
                session.proxies.update({
                    "http": f"http://{proxy}",
                    "https":f"http://{proxy}",
                })

                session.headers = random.choice(goodheaders)
                geo = ""
                print(proxy)
                response = session.get(page_url)
                # print(response.text)
                # breakpoint()
                if response.status_code == 404 or "geo.captcha-delivery.com" not in response.text:
                    return (False, proxy, idx)
                elif response.status_code == 403 or "geo.captcha-delivery.com" in response.text:
                    if 'dd=' in response.text:
                        dd = response.text.split('dd=')[1]
                        dd = dd.split('</script')[0]
                        dd = json.loads(dd.replace("'", '"'))
                        # breakpoint()
                        cid = "".join(response.headers.get('Set-Cookie')).split('datadome=')[1]
                        cid = cid.split(';')[0]
                        try:
                            geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={quote_plus(dd['cid'])}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={quote_plus(page_url)}&s={dd['s']}&e={dd['e']}"
                            cookie = capmonster_solver(website_url=url_with_datadome, captcha_url=geo, cid=cid)
                            return (cookie, proxy, idx)
                        except Exception as e:
                            print("error:", str(e))
                            continue

                        # if dd['t'] == "fe":
                        #     return (geo, cid)
            except Exception as e:
                print("error2:", str(e))
                continue

def format_proxy(px: str):
    if '@' not in px:
        sp = px.split(':')
        if len(sp) == 4:
            px = f'{sp[2]}:{sp[3]}@{sp[0]}:{sp[1]}'
    return {"http": f"http://{px}", "https": f"http://{px}"}


def parse():
    def func_captcha_url(url_with_datadome, proxy):
        session = TlsSession("chrome_120") 
        session.proxies.update({
            "http": f"http://{proxy}",
            "https":f"http://{proxy}",
        })
        ipurl="http://ip-api.com/json"
        response = session.get(ipurl)
        print("func",response.json()['query'])

        page_url = url_with_datadome
        print(url_with_datadome)
        while True:
            try:
                # headerchoice = random.choice(acceptedheaders)
                headerchoice = productheaders.copy()

                headerchoice['origin'] = url_with_datadome
                headerchoice['referer'] = url_with_datadome
                session.headers.update(headerchoice)
                # breakpoint()
                geo = ""
                print(proxy)
                
                response = session.get(page_url)
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
                        geo = f"https://geo.captcha-delivery.com/captcha/?initialCid={quote_plus(dd['cid'])}&hash={dd['hsh']}&cid={cid}&t={dd['t']}&referer={quote_plus(page_url)}&s={dd['s']}&e={dd['e']}"
                        if dd['t'] == "fe":
                            # return (geo, cid)
                            cookie = capmonster_solver(website_url=url_with_datadome, captcha_url=geo, cid=cid)
                        else:
                            continue
                        return cookie
                    else:
                        print("No dd")
                        continue
            except Exception as e:
                print("error from func_captcha_url:", str(e))
                continue

    urls = ["https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/", "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CC8Q/", "https://www.hermes.com/us/en/product/mesh-surligne-rib-trim-jacket-H453420HE1A50/"]
    idx = 0
    
    proxy = random.choice(proxypools)
    cookies = False
    while True:
        # session = Session("chrome_120")
        # session = Session()
        if idx == len(urls):
            break
        url = urls[idx]
        proxies = {
            "http": f"http://{proxy}",
            "https":f"http://{proxy}",
        }
        productheaders["referer"] = url
        productheaders["origin"] = url
        # session.headers = productheaders
        # session.headers.update(productheaders)
        ipurl="http://ip-api.com/json"
        response = requests.get(ipurl, proxies=proxies)
        print("parse",response.json()['query'])
        response = requests.get(url, proxies=proxies, cookies=cookies, headers=productheaders)
        # breakpoint()
        if response.status_code == 403:
            cookie = func_captcha_url(url_with_datadome=url, proxy=proxy)
        # result = capmonster_solver(website_url=url, captcha_url=captcha_url, cid=cid)
        
        if cookie:
            # breakpoint()
            cookieupdate = cookie.split(";")[0]
            # productheaders['cookie'] = f"datadome={cookieupdate}"
            # session.headers.update(productheaders)
            cookies = {
                'datadome':cookieupdate
            }
        else:
            print("Retried to t=fe", url)
            proxy = random.choice(proxypools)
            continue
        # session.headers = productheaders
        # session = Session()
        response = requests.get(ipurl, proxies=proxies)
        print("parse2",response.json()['query'])
        # breakpoint()
        response = requests.get(url, proxies=proxies, headers=productheaders, cookies=cookies, timeout=(20, 20))
        if response.status_code == 403:
            print("Retried for", url)
            proxy = random.choice(proxypools)
            continue
        if response.status_code == 404:
            print("Product Empty")
        else:
            print("Product Available")
        idx += 1


if __name__ == '__main__':
    parse()