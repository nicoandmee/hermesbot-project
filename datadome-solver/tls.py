from tls_client import Session
import json
from browserforge.fingerprints import Screen, FingerprintGenerator
from browserforge.headers import Browser, HeaderGenerator
import time
import random
import datetime

session = Session("chrome_120") 
page_url = 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'

# 1. Load the page
proxies = ["u0a8c217b562505b8-zone-custom-region-cn-st-shanghai:u0a8c217b562505b8@43.159.28.126:2333",
           "u0a8c217b562505b8-zone-custom-region-id-st-jakarta:u0a8c217b562505b8@43.152.113.55:2333",
           "u0a8c217b562505b8-zone-custom-region-sg:u0a8c217b562505b8@43.152.113.55:2333",
           "u0a8c217b562505b8-zone-custom-region-us:u0a8c217b562505b8@43.159.28.126:2333",
           ]
passed = []
goodheaders=[{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/124.0.6367.111 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}, 
 {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/123.0.6312.52 Mobile/15E148 Safari/604.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=1.0', 'Sec-Fetch-Dest': 'navigate', 'Sec-Fetch-Mode': 'same-site', 'Sec-Fetch-Site': '?1', 'Origin': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', 'Referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55'}]
try:
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
                            passed.append(str(datetime.datetime.now()))
                            break
                        print(geo)
                    else:
                        possible_paths = ["/captcha/", "/interstitial/"]
                        for path in possible_paths:
                            start_index = response.text.find(f"https://geo.captcha-delivery.com{path}")
                            if start_index != -1:
                                end_index = response.text.find('"', start_index)
                                geo =  response.text[start_index:end_index]
                if geo =="":
                    geo =  "Not DataDome Captcha / Challenge found"
            # print(geo)
        except Exception as e:
            # breakpoint()
            print(str(e))
            continue
except:
    # exit()    
    breakpoint()


