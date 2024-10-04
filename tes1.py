import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,id;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.hermes.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'initialCid': 'AHrlqAAAAAMALwMGLfF4--EA8OQWMg==',
    'hash': '2211F522B61E269B869FA6EAFFB5E1',
    'cid': 'Aee6dPihFtNqvKXhkZZDYPmsrWzxxxM8TiK9wjv4HFnaaT8P_iKcYF7ImWZDQA~HG41deVW6NBeEJCq~ocv5J4pE0DTfivRQbaCNa9L9alYJGRC5QXaQI4MajQ4y2cwC',
    't': 'fe',
    'referer': 'https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/',
    's': '13461',
    'e': 'fda31eb1d752fe85f97c47d4f51ff2547e37e30d49ee12ee5b2bbff4fd8f0097',
    'dm': 'cd',
}

response = requests.get('https://geo.captcha-delivery.com/captcha/', params=params, headers=headers)
breakpoint()