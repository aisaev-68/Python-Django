import requests

headers = {
    "apikey": "c04dff00-cd68-11ed-b146-19255e2a637a"
}

params = (
   ("url","https://httpbin.org/ip"),
   ("premium","true"),
   ("country","de"),
   ("render","true"),
)

response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params)
print(response.text)

#https://www.g2.com/products/zapier/reviews