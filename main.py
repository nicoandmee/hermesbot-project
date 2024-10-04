

# pip install requests
import requests
import time
 
api_key = "CAP-84A565EA65550AF1518A61A2F07079D3"  # TODO: your api key of capsolver
http_proxy = {"http":"http://spm9mlk9ik:3TlhzhsLf~D7g60Pyj@us.smartproxy.com:10002", "https":"http://spm9mlk9ik:3TlhzhsLf~D7g60Pyj@us.smartproxy.com:10002"}
def capsolver():
    payload = {
        "clientKey": api_key,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": "https://www.hermes.com/us/en/product/hooded-auto-coat-H461320H40150",
            "captchaUrl": "https://geo.captcha-delivery.com/interstitial/?initialCid=AHrlqAAAAAMA5OEH0v8mPZUAtPMgCQ%3D%3D&hash=2211F522B61E269B869FA6EAFFB5E1&cid=2js_MKgVfEn7oURvlgKZcAZRMbNlm7EE7Po9ZEUvel8PJK85xcROHb1tUZwu_7TrpvxwIjZfjwyQQ6kzEUm2ZI2YK~ig35dmQWthRAOoviCNDuBVCFiZIsmJE6gHsQVE&referer=https%3A%2F%2Fwww.hermes.com%2Fus%2Fen%2Fproduct%2Fhooded-auto-coat-H461320H40150%2F&s=13461&b=811355&dm=cd",
            "proxy": "us.smartproxy.com:10001:spm9mlk9ik:3TlhzhsLf~D7g60Pyj",
            # "proxy": "us-ca.proxymesh.com:31280",
		    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            # http://spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:10001
        }

    }
    # http://spm9mlk9ik:3TlhzhsLf~D7g60Pyj@gate.smartproxy.com:7000
    res = requests.post("https://api.capsolver.com/createTask", json=payload)
    resp = res.json()
    task_id = resp.get("taskId")
    if not task_id:
        print("Failed to create task:", res.text)
        return
    print(f"Got taskId: {task_id} / Getting result...")
 
    while True:
        time.sleep(1)  # delay
        payload = {"clientKey": api_key, "taskId": task_id}
        res = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
        resp = res.json()
        status = resp.get("status")
        if status == "ready":
            return resp.get("solution", {}).get("cookie")
        if status == "failed" or resp.get("errorId"):
            print("Solve failed! response:", res.text)
            return
 
cookie = capsolver()
print(cookie)
cookiefix = str(cookie).split(";")[0].replace("datadome=","")


cookies = {'datadome': 'ertMTfiNkTs_FEUO0JPm5bu~h6SZ0~YhJdHzcqseHfeAVY76jmaxiknKVDvqy5i1WDcoqooWUQV6ejfAasXejLAk2TNg_34dBy2iM1RCumyOH4kvtNrw2RmyWjymdO4V'}
cookies = {'datadome': '2js_MKgVfEn7oURvlgKZc6N4jAGutpLgqrl8PTNwmV_d9tcOZZmOgVY1NLyrscEGpEKfZtnxDxPT9o~RzYKtm60Hw8Y4KA5R8aTM8a8c8XNA6s9VrMKObojHh7QPoKYp'}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga_Y862HCHCQ7=GS1.1.1727359836.3.1.1727360670.0.0.0; __cf_bm=DxTH36bRUxxWS63mEFJ.gNXCNWLjDQux3Pd8.mGmVK8-1727386101-1.0.1.1-yVyh1gu0DKvRglrmMwoQltFpBMATxRkm1cWzCM03V7nHcFBVWdKQ1rvrPgpLNEWWkdhOb9YkUh3tBzYUjV0NoQ; datadome=_RPoxQVAsOaL0nnCyCiyURVMJt1J5NCMUDgtDwm3wYPXF2qko1aupyuSnuq881MqhdPq2hI2vexPbvUJ9BNKfV4HH~xE~ndypTI2GQ3doa9JLqTdZknYHRUSP9QoPL2o',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}

response = requests.get('https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK8Q/', cookies=cookies, headers=headers, proxies=http_proxy)
breakpoint()