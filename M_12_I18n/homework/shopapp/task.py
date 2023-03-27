import json
# from .models import Product
import requests
from bs4 import BeautifulSoup

url = "https://real-time-product-search.p.rapidapi.com/search"

querystring = {"q":"apple","country":"ru","language":"ru","page":"1","product_condition":"USED"}

headers = {
	"X-RapidAPI-Key": "111d49d14amshacfe165124e6a53p10ddddjsnd0cfdad67d66",
	"X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)
#
# with open('product0.json', mode='w', encoding='utf-8') as f:
# 	f.write(response.text)


with open('product0.json', mode='r', encoding='utf-8') as f:
	data = json.load(f)

def main():
	lst = ['Смартфон Apple iPhone 12 64GB (фиолетовый)', 'Смартфон Apple iPhone SE 32Gb', 'Смартфон iPhone 8 Plus, 64 GB Apple', 'Apple iPhone 7 32GB Rose Gold', 'Смартфон iPhone XR 64GB Apple', 'Смартфон Apple iPhone 13 mini 128GB (Синий)', 'Смартфон Apple iPhone 11 64GB', 'Смартфон iPhone X 256Gb Apple', 'Наушники Apple AirPods 2', 'Смартфон iPhone 11 Pro 256GB Apple', 'Apple Наушники AirPods Pro', 'Apple iPhone 7 32GB Black', 'Apple iPhone 12 Pro Max 128GB Золотой', 'Смартфон iPhone 8, 256Gb Apple', 'Смартфон Apple iPhone 12 128GB', 'Apple iPhone X 256 Gb Silver', 'Смартфон iPhone 11 Pro Max 256GB Apple']
	data_list = []
	for i, d in enumerate(data['data']):


		if d.get('product_title') in lst:
			# print(d.get('product_title'))
			# print(d.get('product_description'))
			# print(d.get('product_attributes'))
			# print(d.get('product_rating'))
			# print(d.get('product_photos'))
			a = BeautifulSoup(d.get('offer').get('price'), 'html.parser').get_text()
			print(a)


	# 			data_list.append(Product(
	# 					name=d.get('product_title'),
	# 					description=d.get('product_description'),
	# 					attributes=d.get('product_attributes'),
	# 					rating=d.get('product_rating'),
	# 					price=int((d.get('offer').get('price')).split(' ')[0]),
	# 					discount=2,
	# 					products_count=50,
	# 					archived=False,
	# 				)
	# 			)
	#
	# Product.objects.bulk_create(data_list)

main()