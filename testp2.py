#!/usr/bin/env python3

import requests
#geo.iproyal.com:12321:qCVIVja9MOwhXLdq:agcOHyRhV4b6DWCn_country-us_city-tallahassee
# gate.smartproxy.com:10001:spm9mlk9ik:3TlhzhsLf~D7g60Pyj
username = "spm9mlk9ik"
password = "3TlhzhsLf~D7g60Pyj"
PROXY_DNS = "gate.smartproxy.com:10001"

# gate.smartproxy.com:10002:spm9mlk9ik:3TlhzhsLf~D7g60Pyj
username2 = "spm9mlk9ik"
password2 = "3TlhzhsLf~D7g60Pyj"
PROXY_DNS2 = "gate.smartproxy.com:10002"

urlToGet = "http://ip-api.com/json"
while True:
    proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_DNS)}
    r = requests.get(urlToGet , proxies=proxy)

    print("Response:{}".format(r.text))
    proxy = {"http":"http://{}:{}@{}".format(username2, password2, PROXY_DNS2)}
    r = requests.get(urlToGet , proxies=proxy)

    print("Response:{}".format(r.text))    