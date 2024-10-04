import requests

url = 'https://ipv4.icanhazip.com'
proxy = 'geo.iproyal.com:12321'
proxy_auth = 'qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_city-tallahassee'
proxies = {
    'http': f'http://{proxy_auth}@{proxy}',
    'https': f'http://{proxy_auth}@{proxy}'
}

response = requests.get(url, proxies=proxies)
print(response.text)