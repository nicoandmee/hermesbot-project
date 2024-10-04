import requests, random, json
import time
domain = "https://www.hermes.com" # DOMAIN HERE 

def cookiegen(domain):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'api-js.datadome.co',
        'Origin': "https://"+domain.partition("https://")[2],
        'Referer':"https://"+domain.partition("https://")[2],
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    payload = {
        'ddv': '4.6.0',
        'eventCounters': [],
        'jsType': 'ch',
        'ddk': '2211F522B61E269B869FA6EAFFB5E1',
        'events': [],
        'request': '%2F',
        'responsePage': 'origin',
        'cid': "null",
        'dddomain': "https://"+domain.partition("https://")[2],
        'Referer': '',
        'jsData':{
            "ttst": f'{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}',
            "ifov": False,
            "tagpu": f'{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}',
            "glvd": "Google Inc. (NVIDIA)",
            "glrd": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "hc": 16,
            "br_oh": 1040,
            "br_ow": 1920,
            "ua": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)",
            "wbd": False,
            "wdif": False,
            "wdifrm": False,
            "npmtm": False,
            "br_h": 969,
            "br_w": 963,
            "nddc": 1,
            "rs_h": 1080,
            "rs_w": 1920,
            "rs_cd": 24,
            "phe": False,
            "nm": False,
            "jsf": False,
            "lg": "en-US",
            "pr": 1,
            "ars_h": 1040,
            "ars_w": 1920,
            "tz": 480,
            "str_ss": True,
            "str_ls": True,
            "str_idb": True,
            "str_odb": True,
            "plgod": False,
            "plg": random.randint(5, 14),
            "plgne": True,
            "plgre": True,
            "plgof": False,
            "plggt": False,
            "pltod": False,
            "hcovdr": False,
            "hcovdr2": False,
            "plovdr": False,
            "plovdr2": False,
            "ftsovdr": False,
            "ftsovdr2": False,
            "lb": False,
            "eva": 33,
            "lo": False,
            "ts_mtp": 0,
            "ts_tec": False,
            "ts_tsa": False,
            "vnd": "Google Inc.",
            "bid": "NA",
            "mmt": "application/pdf,text/pdf",
            "plu": "PDF Viewer,Chrome PDF View"
        }
    }
    response = requests.post("https://api-js.datadome.co/js/", headers=headers, data=payload)
    data = json.loads(response.text)
    if "cookie" in response.text:
        print('Successfully genned cookie')
        # print(data['cookie'])
    else:
        print('Error while genning cookie')
        # print(data)
    return data
data = cookiegen(domain)
cookiefix = str(data['cookie']).split(";")[0].replace("datadome=","")

breakpoint()
cookies = {
    'OptanonAlertBoxClosed': '2024-09-06T23:13:41.852Z',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Sep+23+2024+21%3A05%3A50+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=77cdf23d-5ec9-4924-ab05-141c150189c1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ID%3BMU&AwaitingReconsent=false',
    'GeoFilteringBanner': '1',
    '_ga': 'GA1.1.347384777.1725664395',
    '_gcl_au': '1.1.581039184.1725664395',
    '_cs_c': '1',
    'rskxRunCookie': '0',
    'rCookie': 'z0lfedlqnkwzaui3ws57m0rc0ylc',
    'x-xsrf-token': 'eba595ab-6817-4bae-87ad-fde1058cfa24',
    'correlation_id': '2vdq0kno2ldgutt3omjymxvnumu7n52wqmrxl239dpbo39wf7xttjxordni5376e',
    'locale-country-data': '{"country":"us","locale":"en-he","language":"en"}',
    '_uetvid': '94193ba078a911efbe2a9b9021985a68',
    '_fbp': 'fb.1.1726986330099.204574573627742676',
    '_cs_cvars': '%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22single%20product%20page%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Hooded%20sweater%20%7C%20Herm%C3%A8s%20USA%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22MEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22MENREADYTOWEAR%22%5D%2C%226%22%3A%5B%22in_store_only%22%2C%22no%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22H%22%5D%2C%229%22%3A%5B%22category%22%2C%22H%2FH29%22%5D%2C%2210%22%3A%5B%22editorialcategory%22%2C%22LANDITO_SACS_LINDY%22%5D%2C%2212%22%3A%5B%22productcode%22%2C%22H457800HA01XL%22%5D%7D',
    'ECOM_SESS': '06fn6bjrqhd7jlnalud9k7ec2x',
    '__cf_bm': 'f_Ds4kYs._r..tiJagys_aAhgwVfcRnrB3dlvMAh_ss-1727093147-1.0.1.1-faesDLYt1NU4K4UPdd3hp3xaZFAtAazzcwg73GklzkJYp_PyfYJ0PDQBf3yexQ1IvSTc1KGuz2f_0DxM757RNQ',
    '_cs_mk': '0.6425478586685334_1727093150982',
    '_ga_Y862HCHCQ7': 'GS1.1.1727091954.9.1.1727093150.0.0.0',
    '_cs_id': '73388519-527b-ae60-fb37-1ec777f06a65.1725664395.8.1727093151.1727091928.1.1759828395804.1',
    '_cs_s': '2.0.0.1727094951149',
    'lastRskxRun': '1727093153484',
    # 'datadome': 'w1vezEh95Gzg49N4boPhgrBHfUHdsz9MfajeCyyaoSm12b~JJDz08mNREd87ePMVOU3iuWxQpNU73YZLq52_KTApckygwAgV8u0Rs7anp6Ge8lFTsFga8o6lltHBpYw9',
    'datadome': cookiefix    
    # Max-Age=31536000; Domain=.hermes.com; Path=/; Secure; SameSite=Lax
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}
proxies = {
    "http": "http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
    "https":"http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
}
headers['datadome'] = cookiefix
while True:
    response = requests.get('https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/',  headers=headers)
    
    breakpoint()
    if response.text.find("You have been blocked.") != -1:
        print("IP Blocked")
    else:
        print("Run")
    time.sleep(5)
