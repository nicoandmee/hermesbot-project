import requests

proxies = {
  "http": "192.126.135.189:8800",
  "https": "192.126.135.189:8800"
}
response = requests.get('https://quotes.toscrape.com/', proxies=proxies)
print(response.text)

      