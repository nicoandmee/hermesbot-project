import requests

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
    'datadome': '84nOSPVsMh5FHARy~VwtnybvfNndI_dgAwn_rKraxcV0yWl8AzMg78H34sS0txXiir8EUUFer2QkNDqNGIk8JKgwfqUs4tj7x4_L~Jfz83RrxtDX9mGpngfVZ54QlMTo',
    '__cf_bm': '5BMSD3sf3m99Y.v0AFfAShBWnsPedDwAobAiLuZuZE8-1727221226-1.0.1.1-dXZp5yXt086VKUtOF.eK_Mue_eoGn11pRMUSbTJsByJjbwsUHN.gP8U4W_sNNW4rZVJxE5l2L2OYdW.wFnOb_w',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'OptanonAlertBoxClosed=2024-09-06T23:13:41.852Z; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Sep+23+2024+21%3A06%3A09+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=77cdf23d-5ec9-4924-ab05-141c150189c1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=ID%3BMU&AwaitingReconsent=false; GeoFilteringBanner=1; _ga=GA1.1.347384777.1725664395; _gcl_au=1.1.581039184.1725664395; _cs_c=1; rskxRunCookie=0; rCookie=z0lfedlqnkwzaui3ws57m0rc0ylc; x-xsrf-token=eba595ab-6817-4bae-87ad-fde1058cfa24; correlation_id=2vdq0kno2ldgutt3omjymxvnumu7n52wqmrxl239dpbo39wf7xttjxordni5376e; locale-country-data={"country":"us","locale":"en-he","language":"en"}; _uetvid=94193ba078a911efbe2a9b9021985a68; _fbp=fb.1.1726986330099.204574573627742676; _cs_cvars=%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22single%20product%20page%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Hooded%20sweater%20%7C%20Herm%C3%A8s%20USA%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22MEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22MENREADYTOWEAR%22%5D%2C%226%22%3A%5B%22in_store_only%22%2C%22no%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22H%22%5D%2C%229%22%3A%5B%22category%22%2C%22H%2FH29%22%5D%2C%2210%22%3A%5B%22editorialcategory%22%2C%22LANDITO_SACS_LINDY%22%5D%2C%2212%22%3A%5B%22productcode%22%2C%22H457800HA01XL%22%5D%7D; ECOM_SESS=06fn6bjrqhd7jlnalud9k7ec2x; lastRskxRun=1727093169341; _cs_id=73388519-527b-ae60-fb37-1ec777f06a65.1725664395.8.1727093169.1727091928.1.1759828395804.1; _ga_Y862HCHCQ7=GS1.1.1727091954.9.1.1727093753.0.0.0; datadome=84nOSPVsMh5FHARy~VwtnybvfNndI_dgAwn_rKraxcV0yWl8AzMg78H34sS0txXiir8EUUFer2QkNDqNGIk8JKgwfqUs4tj7x4_L~Jfz83RrxtDX9mGpngfVZ54QlMTo; __cf_bm=5BMSD3sf3m99Y.v0AFfAShBWnsPedDwAobAiLuZuZE8-1727221226-1.0.1.1-dXZp5yXt086VKUtOF.eK_Mue_eoGn11pRMUSbTJsByJjbwsUHN.gP8U4W_sNNW4rZVJxE5l2L2OYdW.wFnOb_w',
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

response = requests.get('https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55', cookies=cookies, headers=headers)
breakpoint()