from pathlib import Path
import os
import base64
import capsolver

# tokenTask
capsolver.api_key = "CAP-84A565EA65550AF1518A61A2F07079D3"
print("api host",capsolver.api_base)
print("api key",capsolver.api_key)
# capsolver.api_key = "..."
solution = capsolver.solve({
        "type":"ReCaptchaV2TaskProxyLess",
        "websiteKey":"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
        "websiteURL":"https://www.google.com/recaptcha/api2/demo",
    })

print(solution)

# RecognitionTask
img_path = os.path.join(Path(__file__).resolve().parent,"queue-it.jpg")
breakpoint()
with open(img_path,'rb') as f:
    solution = capsolver.solve({
        "type":"ImageToTextTask",
        "module":"queueit",
        "body":base64.b64encode(f.read()).decode("utf8")
    })
    print(solution)

# get current balance
balance = capsolver.balance()
# print the current balance
print(balance)