import json
from pathlib import Path

with open(str(Path(__file__).parent.joinpath('json_data-products2.json'))) as json_file:
    data = json.load(json_file)

brend = ["Apple", "Samsung", "Sony", "Xiaomi", "Nokia", "Philips", "Huawei"]
for item in brend:
    for index, prod in enumerate(data["data"]):
        if item in prod["name"]:
            print(data["data"][index])
            data["data"][index]["brand"] = item

# lst = []
# i = 0
# json_products = {}
# for key, value in data.items():
#     lst_prod = []
#
#     for item in value:
#         if not item['name'] in lst:
#
#             lst.append(item["name"])
#             lst_prod.append(item)
#
#     json_products[key] = lst_prod

with open('json_data-products.json', mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)