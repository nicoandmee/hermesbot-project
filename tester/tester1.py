
import requests
import time

api_key = "CAP-84A565EA65550AF1518A61A2F07079D3"
page_url = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55"
proxy = "residential-proxy.scrapeops.io:8181:scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a" 
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
def get_token(captcha_url):
    print("call capsolver...")
    data = {
        "clientKey": api_key,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": page_url,
            "captchaUrl": captcha_url,
            "userAgent": user_agent,
            "proxy": proxy,
        },
    }
    uri = 'https://api.capsolver.com/createTask'
    res = requests.post(uri, json=data)
    resp = res.json()
    task_id = resp.get('taskId')
    if not task_id:
        print("create task error:", res.text)
        return
    while True:
        time.sleep(1)
        data = {
            "taskId": task_id
        }
        res = requests.post('https://api.capsolver.com/getTaskResult', json=data)
        # print(res.text)
        resp = res.json()
        status = resp.get('status', '')
        if status == "ready":
            cookie = resp['solution']['cookie']
            cookie = cookie.split(';')[0].split('=')[1]
            print("successfully got cookie:", cookie)
            return cookie
        if status == "failed" or resp.get("errorId"):
            print("failed to get cookie:", res.text)
            return
        print('solve datadome status:', status)
def format_proxy(px: str):
    if '@' not in px:
        sp = px.split(':')
        if len(sp) == 4:
            px = f'{sp[2]}:{sp[3]}@{sp[0]}:{sp[1]}'
    return {"http": f"http://{px}", "https": f"http://{px}"}
def request_site(cookie):
    headers = {
        'content-type': 'application/json',
        'user-agent': user_agent,
        'accept': 'application/json, text/plain, */*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': page_url,
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
    }
    if cookie:
        headers['cookie'] = "datadome=" + cookie
    print("request url:", page_url)
    # The primary site does not have TLS fingerprinting, and 'requests' can be used
    response = requests.get(
        page_url, headers=headers, proxies=format_proxy(proxy), allow_redirects=True
    )
    print("response status_code:", response.status_code)
    # breakpoint()
    if response.status_code == 403:
        
        resp = response.json()
        print("captcha url: ", resp['url'])
        return resp['url']
    else:
        # print("response:", response.text)
        print('cookie is good!')
        return
def main():
    url = request_site("")
    if not url:
        return
    if 't=bv' in url:
        print("blocked captcha url is not supported")
        return
    cookie = get_token(url)
    if not cookie:
        return
    request_site(cookie)
if __name__ == '__main__':
    main()