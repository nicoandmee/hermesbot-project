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

TELEGRAM_BOT_TOKEN="7207865537:AAEyl4_fIWnFjZTnaH9uN6eJeYUF87MfRAk"
TELEGRAM_CHAT_ID="-1002481993342"
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
# proxypools = [
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20001",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20002",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20003",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20004",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20005",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20006",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20007",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20008",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20009",
#     "http://user-spm9mlk9ik-os-ios:3TlhzhsLf~D7g60Pyj@ca.smartproxy.com:20010",
# ]
# proxypools = [
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-0FZ7vDwE_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-OX22hIzq_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-Dk9CvstP_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-z7KB5SaH_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-BtY4Ccgl_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-APSCmzuz_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-h48fSNQ8_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-TeCMjniX_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-IBii2U8R_lifetime-10m@geo.iproyal.com:12321",
# "qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-ae,id_session-HVEcMywR_lifetime-10m@geo.iproyal.com:12321",
# ]
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
    print("Try to solve Captcha", flush=True, end="")
    while True:
        time.sleep(2)
        res = requests.post('https://api.capmonster.cloud/getTaskResult', headers=headers, json=data2)
        resp = res.json()
        status = resp.get('status', '')
        if status == "ready":
            # breakpoint()
            cookie = resp['solution']['domains']['hermes.com']['cookies']['datadome']
            # cookie = cookie.split(';')[0].split('=')[1]
            # print("successfully got cookie:", cookie)
            print("successfully got cookie")

            return cookie
        if status == "failed" or resp.get("errorId"):
            print("failed to solve datadome:", res.text)
            return
        print('.', flush=True, end="")

def send_to_telegram(message):
    apiToken = TELEGRAM_BOT_TOKEN
    chatID = TELEGRAM_CHAT_ID
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message, "parse_mode": "HTML"})
        # print(response.text)
    except Exception as e:
        print(e)

def parse_to_html(link):
    html = "<strong>Product Available</strong>\n"
    html += f'<a href="{link}">Go to Page</a>'
    return html

def parse():
    def func_captcha_url(url_with_datadome, proxy):
        session = TlsSession("chrome_120") 
        session.proxies.update({
            "http": f"http://{proxy}",
            "https":f"http://{proxy}",
        })
        # ipurl="http://ip-api.com/json"
        # response = session.get(ipurl)
        # print("func",response.json()['query'])

        page_url = url_with_datadome
        # print(url_with_datadome)
        while True:
            try:
                # headerchoice = random.choice(acceptedheaders)
                headerchoice = productheaders.copy()

                headerchoice['origin'] = url_with_datadome
                headerchoice['referer'] = url_with_datadome
                session.headers.update(headerchoice)
                # breakpoint()
                geo = ""
                # print(proxy)
                
                response = session.get(page_url)
                # print(response.text)
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

                        # if dd['t'] == "fe":
                        #     cookie = capmonster_solver(website_url=url_with_datadome, captcha_url=geo, cid=cid)
                        # else:
                        #     continue
                        cookie = capmonster_solver(website_url=url_with_datadome, captcha_url=geo, cid=cid)
                        return cookie
                    else:
                        print("No dd")
                        continue
            except Exception as e:
                # print("error from func_captcha_url:", str(e))
                continue

    urls = [
    "https://www.hermes.com/us/en/product/straight-cut-jeans-H455400H20140/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CC89/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK09/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/",
    "https://www.hermes.com/us/en/product/lindy-26-bag-H073428CK37/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CKT7/",
    "https://www.hermes.com/us/en/product/lindy-26-bag-H073428CK55/",
    "https://www.hermes.com/us/en/product/lindy-26-bag-H073428CK89/",
    "https://www.hermes.com/us/en/product/lindy-26-bag-H073430CC8L/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK18/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK8Q/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CKU4/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK37/",
    "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CC8Q/",
    "https://www.hermes.com/us/en/product/constance-long-to-go-wallet-H080125CK89/",
    "https://www.hermes.com/us/en/product/constance-long-to-go-wallet-H080125CK10/",
    ]
    idx = 0
    
    proxy = random.choice(proxypools)
    cookies = False
    while True:
        if idx == len(urls):
            idx = 0
            continue
        url = urls[idx]
        proxies = {
            "http": f"http://{proxy}",
            "https":f"http://{proxy}",
        }
        productheaders["referer"] = url
        productheaders["origin"] = url
        print(url, '...', flush=True, end="")
        response = requests.get(url, proxies=proxies, cookies=cookies, headers=productheaders)
        if response.status_code == 403:
            print("Failed")
            cookie = func_captcha_url(url_with_datadome=url, proxy=proxy)
        else:
            if response.status_code == 404:
                print("Product Empty")
            else:
                html = parse_to_html(link=url)
                send_to_telegram(html)
                print("Product Available")
            idx += 1
            continue
        

        if cookie:
            cookieupdate = cookie.split(";")[0]
            cookies = {
                'datadome':cookieupdate
            }
        else:
            # print("Retried to t=fe", url)
            proxy = random.choice(proxypools)
            idx += 1
            continue
        print(url, '...', flush=True, end="")
        for _ in range (0,10):
            response = requests.get(url, proxies=proxies, headers=productheaders, cookies=cookies, timeout=(20, 20))
            if response.status_code != 403:
                break
        if response.status_code == 403:
            print("Failed")
            proxy = random.choice(proxypools)
            continue
        
        if response.status_code == 404:
            print("Product Empty")
        else:
            html = parse_to_html(link=url)
            send_to_telegram(html)
            print("Product Available")
        idx += 1


if __name__ == '__main__':
    while True:
        try:
            parse()
        except:
            time.sleep(60*3)
            continue