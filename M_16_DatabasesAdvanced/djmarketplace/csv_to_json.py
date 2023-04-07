import csv
import json
import random

from bs4 import BeautifulSoup

# category,subcategory2,subcategory3,article,mode_article,name,
# path,price,old_price,price_zakupki,count,description,short_description,
# brand,Вес,Meta title,Meta keywords,Meta description,Фото (через пробел),link,attributes,color

with open('phones.csv', 'r', newline='') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    reader = csv.DictReader(csvfile)
    prod = {}
    lst = []
    for row in reader:
        # print(row["category"], row["article"], row["name"], row["price"])
        a = row["Ссылки на фото (через пробел)"].split(" ")
        s = BeautifulSoup(row["Характеристики (HTML/Table)"], 'html.parser')
        d = s.findAll('td')
        # lst.append(s)
        print(d)
        l = []
        data = {}
        for ind, item in enumerate(d):

            if (ind + 1) % 2 == 0:
                data[str(BeautifulSoup(str(d[ind - 1]), 'html.parser').get_text())] = str(BeautifulSoup(str(d[ind]), 'html.parser').get_text())

        print(data)

        break
    #     if len(a) > 1:
    #         link = a[1:]
    #     else:
    #         link = a
    #
    #     product = {
    #         "name": row["Имя товара"][18:],
    #         "brand": row["Производитель"],
    #         "description": row["Описание"],
    #         "attributes": row["Характеристики (HTML/Table)"],
    #         "rating": round(random.uniform(0, 5), 1),
    #         "image": link,
    #         "price": row["Цена"].replace(" ", "").replace(",", "."),
    #         "discount": random.choices([3, 5, 10, 15, 20])[0],
    #         "products_count": 50,
    #         "archived": False,
    #         "sold": random.choices([x + 1 for x in range(50)])[0],
    #         }
    #     lst.append(product)
    # print(len(lst))
    # prod["phones"] = lst
    # with open('json_data-phones.json', mode='w', encoding='utf-8') as f:
    #     json.dump(prod, f, ensure_ascii=False, indent=4)