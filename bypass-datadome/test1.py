import requests

cookies = {
    'OptanonAlertBoxClosed': '2024-09-25T13:20:56.171Z',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Sep+26+2024+06%3A52%3A32+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8cadd951-2d1d-4f84-ba7c-1354960b65d9&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=ID%3BMU',
    'GeoFilteringBanner': '1',
    '_ga': 'GA1.1.4416237.1727270456',
    '_gcl_au': '1.1.766724459.1727270457',
    '_cs_c': '1',
    'rskxRunCookie': '0',
    'rCookie': 'm68ti6yl8ua50rszvwy082m1hw8i07',
    '_uetsid': '00bece207b4111efaa004b9d09ff15b1',
    '_uetvid': '00bf12a07b4111ef864cf5ad02a1b4e3',
    'x-xsrf-token': '25dbfb86-b1a8-43ae-a9dd-4520d6a65b57',
    'ECOM_SESS': 'ehmdakzus1z6qn5afgsbp0434h',
    'correlation_id': 'oeb8yns9ckcv3ldu66c6lzzvb7faz08v9ufohdlaixa3vq5z7ajlir1t4uukah6o',
    '_cs_cvars': '%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22single%20product%20page%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Hooded%20auto%20coat%20%7C%20Herm%C3%A8s%20USA%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22MEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22MENREADYTOWEAR%22%5D%2C%226%22%3A%5B%22in_store_only%22%2C%22no%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22H%22%5D%2C%229%22%3A%5B%22category%22%2C%22H%2FH20%22%5D%2C%2212%22%3A%5B%22productcode%22%2C%22H461320H40150%22%5D%7D',
    '_fbp': 'fb.1.1727270516513.753951651614570',
    '__cf_bm': 'vCZ53i1kKu6NuqLrZMzgMZJJ5qSr.6cniHfl5IB5r80-1727300591-1.0.1.1-6E0Gbd5eRE.cmqntLCJIwgvBRuBbuSIV1smw2jiBmLVEjF3qK2iIRi_0CZG85wsgHr5td84ZaXFtqptzR07ygA',
    '_cs_mk': '0.19509414924740853_1727300608804',
    '_ga_Y862HCHCQ7': 'GS1.1.1727300608.3.1.1727301151.0.0.0',
    'lastRskxRun': '1727301152099',
    '_cs_id': 'd3247bf6-e37d-a658-f66d-19b1355a8cca.1727270458.2.1727301152.1727297963.1.1761434458701.1',
    'datadome': 'cE93RuHxP35GdV3Axfog73Eme7AHOQzcnHmU3uZ~rpN~IuZwv_zEJBwYyjkVQDhNRrveSiqkn2418Zmj6~GlkTSXH9_yviyRVASo3F~MSnCqnRC8GWOz0LljElJWRGFz',
    '_cs_s': '7.0.0.1727303043835',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Wed, 25 Sep 2024 21:43:28 GMT',
    'priority': 'u=0, i',
    'referer': 'https://www.hermes.com/us/en/product/hooded-auto-coat-H461320H40150/',
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
    # "datadome": "cE93RuHxP35GdV3Axfog73Eme7AHOQzcnHmU3uZ~rpN~IuZwv_zEJBwYyjkVQDhNRrveSiqkn2418Zmj6~GlkTSXH9_yviyRVASo3F~MSnCqnRC8GWOz0LljElJWRGFz"
}

response = requests.get(
    'https://www.hermes.com/us/en/product/hooded-auto-coat-H461320H40150/',
    cookies=cookies,
    headers=headers,
)
breakpoint()