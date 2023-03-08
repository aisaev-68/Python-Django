import json
import os

dict_prod = {'Электроника': 'text.txt', 'Бытовая техника': 'text1.txt', 'Красота и здоровье': 'text2.txt',
             'Одежда': 'text3.txt', 'Обувь': 'text4.txt', 'Строительство и ремонт':'text5.txt', 'Детские товары': 'text6.txt'}
catalog = []
for key, value in dict_prod.items():
    with open(value, mode='r', encoding='utf-8') as f:
        data = f.readlines()

    lst1 = {}
    lst2 = {}
    d = {}
    for item in data:
        if item.startswith('1'):
            lst_d = []
            k = item[1:].strip()
        else:
            lst_d.append(item.strip())
        lst2[k] = lst_d
    lst1[key] = lst2
    catalog.append(lst1)

with open('json_data-categories.json', 'w', encoding='utf-8') as outfile:
    json.dump({'data': catalog}, outfile, indent=4, ensure_ascii=False)

print(catalog)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)