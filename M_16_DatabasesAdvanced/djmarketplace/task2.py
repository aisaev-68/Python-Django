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
#https://ejudge.lksh.ru/lang_docs/djbook.ru/rel1.9/ref/models/querysets.html
#https://www.g2.com/products/zapier/reviews