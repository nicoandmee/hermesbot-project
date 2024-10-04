import capsolver
import requests
capsolver.api_key = "CAP-84A565EA65550AF1518A61A2F07079D3"
PAGE_URL = "https://dd.hermes.com/js/" # Check your country domain, could be vinted.fi or other
# PAGE_URL = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/" # Check your country domain, could be vinted.fi or other

CAPTCHA_URL = "https://geo.captcha-delivery.com/interstitial/?initialCid=AHrlqAAAAAMAdgh4yql-HEkA8ouCOA%3D%3D&hash=2211F522B61E269B869FA6EAFFB5E1&cid=q5tk_DYuDDJN~k7WFWGLnl_QYbeZRp0HfxmmlDEQ8cmiVzWoLnChru8ggy8jFm_MUHIyKZmIwrZ52WkbICN3zylJy1AqFh0GNPrExZI0povAcePuodj4m_XXLNqqCLtl&referer=https%3A%2F%2Fwww.hermes.com%2Fus%2Fen%2Fproduct%2Flindy-ii-mini-bag-H085956CK55%2F&s=13461&b=811355&dm=cd"
PROXY = "residential-proxy.scrapeops.io:8181:scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a"

def solver_datadome(url, captchaURL, proxy):
    solution = capsolver.solve({
        "type": "DatadomeSliderTask",
        "websiteURL": url,
        "captchaURL": captchaURL,
        "proxy": proxy,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    })
    
    return solution

def main():
    print("Solving DataDome Vinted")
    # Remember Captcha_URL, the query params must be obtained dynamic, you can't use the same captcha url over and over. Please read our blog to understand how.
    solution = solver_datadome(PAGE_URL, CAPTCHA_URL, PROXY)
    print("Solution: ", solution)
    # breakpoint()
    

    cookies = {
        'OptanonAlertBoxClosed': '2024-09-06T23:13:41.852Z',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Sep+23+2024+21%3A06%3A09+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=77cdf23d-5ec9-4924-ab05-141c150189c1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ID%3BMU&AwaitingReconsent=false',
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
        'lastRskxRun': '1727093169341',
        '_cs_id': '73388519-527b-ae60-fb37-1ec777f06a65.1725664395.8.1727093169.1727091928.1.1759828395804.1',
        '_ga_Y862HCHCQ7': 'GS1.1.1727091954.9.1.1727093753.0.0.0',
        '__cf_bm': 'TZMpr7pc6mJhcw03WlJArDibnZwbLj8GCuuNqQMAxxw-1727226369-1.0.1.1-RMK5xC0Mbce8JnZia04PvQbNZ5NX8Hggvpu6cU01cNinzi1focovlu8qhET0wD73U3hwI9qEvsBsUnk4GboNcA',
        'datadome': 'M5iLuwptcbWSr4p_Mj9Q~_mh55FW922DRaTo9oBcFg83Wca1Tvhd9297brUJuOJDAymvx6hkZ3hLBfNpCP1EVwpfyGo78xxLAr~JKB69vueLcEuyo_TV6Ot5fTjdZx2V',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'OptanonAlertBoxClosed=2024-09-06T23:13:41.852Z; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Sep+23+2024+21%3A06%3A09+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=77cdf23d-5ec9-4924-ab05-141c150189c1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ID%3BMU&AwaitingReconsent=false; GeoFilteringBanner=1; _ga=GA1.1.347384777.1725664395; _gcl_au=1.1.581039184.1725664395; _cs_c=1; rskxRunCookie=0; rCookie=z0lfedlqnkwzaui3ws57m0rc0ylc; x-xsrf-token=eba595ab-6817-4bae-87ad-fde1058cfa24; correlation_id=2vdq0kno2ldgutt3omjymxvnumu7n52wqmrxl239dpbo39wf7xttjxordni5376e; locale-country-data={"country":"us","locale":"en-he","language":"en"}; _uetvid=94193ba078a911efbe2a9b9021985a68; _fbp=fb.1.1726986330099.204574573627742676; _cs_cvars=%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22single%20product%20page%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Hooded%20sweater%20%7C%20Herm%C3%A8s%20USA%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22MEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22MENREADYTOWEAR%22%5D%2C%226%22%3A%5B%22in_store_only%22%2C%22no%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22H%22%5D%2C%229%22%3A%5B%22category%22%2C%22H%2FH29%22%5D%2C%2210%22%3A%5B%22editorialcategory%22%2C%22LANDITO_SACS_LINDY%22%5D%2C%2212%22%3A%5B%22productcode%22%2C%22H457800HA01XL%22%5D%7D; ECOM_SESS=06fn6bjrqhd7jlnalud9k7ec2x; lastRskxRun=1727093169341; _cs_id=73388519-527b-ae60-fb37-1ec777f06a65.1725664395.8.1727093169.1727091928.1.1759828395804.1; _ga_Y862HCHCQ7=GS1.1.1727091954.9.1.1727093753.0.0.0; __cf_bm=TZMpr7pc6mJhcw03WlJArDibnZwbLj8GCuuNqQMAxxw-1727226369-1.0.1.1-RMK5xC0Mbce8JnZia04PvQbNZ5NX8Hggvpu6cU01cNinzi1focovlu8qhET0wD73U3hwI9qEvsBsUnk4GboNcA; datadome=M5iLuwptcbWSr4p_Mj9Q~_mh55FW922DRaTo9oBcFg83Wca1Tvhd9297brUJuOJDAymvx6hkZ3hLBfNpCP1EVwpfyGo78xxLAr~JKB69vueLcEuyo_TV6Ot5fTjdZx2V',
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
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    session = requests.Session()
    response = session.get('https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/', cookies=cookies, headers=headers)
    cookie = solution["cookie"].split("datadome=")[1].split("; ")[0]
    # breakpoint()
    session.cookies.set("datadome", cookie)
    # breakpoint()
    proxies = {
    "http": "http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
    "https":"http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
}

    response = session.get('https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/', headers={
        "authority": "www.hermes.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-GB,en;q=0.9",
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Google Chrome";v="110", "Chromium";v="110", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}, proxies=proxies)
    breakpoint()

main()