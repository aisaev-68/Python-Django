
dict_prod = {'Электроника': 'text.txt', 'Бытовая техника': 'text1.txt', 'Красота и здоровье': 'text2.txt',
             'Одежда':'text3.txt', 'Обувь': 'text4.txt', 'Строительство и ремонт':'text5.txt', 'Детские товары': 'text6.txt'}
catalog = []
for key, value in dict_prod.items():
    with open(value, mode='r', encoding='utf-8') as f:
        data = f.readlines()

    lst1 = {}
    lst2 = {}
    d = {}
    dict_electron = {'Электроника': lst1, 'Бытовая техника': lst2}
    for item in data:
        if item.startswith('1'):
            lst_d = []
            k = item[1:].strip()
        else:
            lst_d.append(item.strip())
        lst2[k] = lst_d
    lst1[key] = lst2
    catalog.append(lst1)


print(catalog)