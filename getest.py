
# pip install requests
import requests
import time

api_key = "CAP-84A565EA65550AF1518A61A2F07079D3"  # TODO: your api key of capsolver

def capsolver():
    payload = {
        "clientKey": api_key,
        "task": {
            "type": 'DatadomeSliderTask',
            "websiteURL": "https://www.hermes.com",
            "captchaUrl": "https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMA1QGvUmJwyYoAwpyjNg%3D%3D&hash=789361B674144528D0B7EE76B35826&cid=6QAEcL8coBYTi9tYLmjCdyKmNNyHz1xwM2tMHHGVd_Rxr6FsWrb7H~a04csMptCPYfQ25CBDmaOZpdDa4qwAigFnsrzbCkVkoaBIXVAwHsjXJaKYXsTpkBPtqJfLMGN&t=fe&referer=https%3A//www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/",
            "proxy": "residential-proxy.scrapeops.io:8181:scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a",
		    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
    }
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

