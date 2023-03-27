import json
import random

# from .models import Product
import requests

from bs4 import BeautifulSoup

url = "https://real-time-product-search.p.rapidapi.com/search"


# querystring = {"q":"huawei","country":"ru","language":"ru","page":"1","product_condition":"USED"}
#
# headers = {
# 	"X-RapidAPI-Key": "111d49d14amshacfe165124e6a53p10ddddjsnd0cfdad67d66",
# 	"X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# with open('product6.json', mode='w', encoding='utf-8') as f:
# 	f.write(response.text)

# brend = ["Apple", "Samsung", "Sony", "Xiaomi", "Nokia", "Philips", "Huawei"]
# list_brend = {}
# for ind, item in enumerate(brend):
#     with open(f'product{str(ind)}.json', mode='r', encoding='utf-8') as f:
#         data = json.load(f)
#     list_brend[item] = data["data"]
#
# with open('product.json', mode='w', encoding='utf-8') as f:
# 	json.dump(list_brend, f, ensure_ascii=False, indent=4)
#
def main():
    with open(f'product.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)
    prod = {}
    lst = []
    c = "Все подробности можно узнать на нашем сайте, или позвонив по номеру 88005005513"
    for key, value in data.items():
        for item in value:
            a = BeautifulSoup(item.get('offer').get('price'), 'html.parser').get_text()
            b = a.replace('\xa0', "")[:-1].replace(' ', '').replace(',', '.')
            product = {"name": item.get('product_title'),
                       "description": item.get('product_description') if item.get('product_description') else c,
                       "attributes": item.get('product_attributes') if item.get('product_attributes') else {},
                       "rating": random.choices([1.2, 1.5, 2.0, 2.4, 2.5, 2.7, 3.0, 3.5, 3.9, 4, 4.4, 4.8, 5.0, 0.0])[0],
                       "image": item.get('product_photos'),
                       "price": b if b else 0.0,
                       "discount": random.choices([3, 5, 10, 15, 20])[0],
                       "products_count": 50,
                       "archived": False,
                       "sold": random.choices([x + 1 for x in range(50)])[0],
                       }
            lst.append(product)
        prod[key] = lst
    with open('json_data-products.json', mode='w', encoding='utf-8') as f:
        json.dump(prod, f, ensure_ascii=False, indent=4)


main()
