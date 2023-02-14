import json
import requests
from bs4 import BeautifulSoup
import wget

url = "https://real-time-product-search.p.rapidapi.com/search"

querystring = {"q": "apple", "country": "ru", "language": "ru", "page": "1", "product_condition": "USED"}

headers = {
    "X-RapidAPI-Key": "9d95cc8b95msh151617ccb8cd678p18b0b3jsnea234e546ff3",
    "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)
#
# with open('product.json', mode='w', encoding='utf-8') as f:
#     # f.write(response.text)
#     json.dump(response.json(), f)




#
def main():
    lst = ['Смартфон Apple iPhone 12 64GB (фиолетовый)', 'Смартфон Apple iPhone SE 32Gb',
           'Смартфон iPhone 8 Plus, 64 GB Apple', 'Apple iPhone 7 32GB Rose Gold', 'Смартфон iPhone XR 64GB Apple',
           'Смартфон Apple iPhone 13 mini 128GB (Синий)', 'Смартфон Apple iPhone 11 64GB',
           'Смартфон iPhone X 256Gb Apple', 'Наушники Apple AirPods 2', 'Смартфон iPhone 11 Pro 256GB Apple',
           'Apple Наушники AirPods Pro', 'Apple iPhone 7 32GB Black', 'Apple iPhone 12 Pro Max 128GB Золотой',
           'Смартфон iPhone 8, 256Gb Apple', 'Смартфон Apple iPhone 12 128GB', 'Apple iPhone X 256 Gb Silver',
           'Смартфон iPhone 11 Pro Max 256GB Apple']
    data_list = []
    dd = {}

    with open('product.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)

    for i, d in enumerate(data['data']):

        if d.get('product_title') in lst:

            a = BeautifulSoup(d.get('offer').get('price'), 'html.parser').get_text()
            b = a.replace(u'\xa0', '')[:-1]
            c = b.split(',')[0]
            data_list.append({
                'name': d.get('product_title'),
                'description': d.get('product_description'),
                'attributes': d.get('product_attributes'),
                'rating': d.get('product_rating'),
                'price': int(c),
                'discount': 2,
                'image': d.get("product_photos")[0],
                'products_count': 50,
                'archived': False, }
            )

    dd["data"] = data_list
    # Product.objects.bulk_create(data_list)
    with open('products.json', mode='w', encoding='utf-8') as f:
        json.dump(dd, f)



# main()
# with open('products.json', mode='r', encoding='utf-8') as f:
#     data = json.load(f)
#     print(data)

lst = []
def tets():
    with open('products.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
    for item in data['data']:
        print(item['image'])
        lst.append(item)
        # url = item['image'][0]
        # filename = wget.download(url)
        # if item.get('image'):
        #     print(filename)
            # with open(filename, mode='w', encoding='utf-8') as f:
            #     f.write()
    print(lst)

tets()