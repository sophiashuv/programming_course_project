from translate import Translator
from product import Product
import json
import codecs


def add_product(block, product):
    """
    Creates a Product class item from a dictioanry and adds it to a block of food type.
    (list, dictionary) - > None
    """
    block.append(Product(product['Номер'], product['Продукт'],
                         product['ккал'].replace(',', '.'),
                         product['білок'].replace(',', '.'),
                         product['жири'].replace(',', '.'),
                         product['вуглеводи'].replace(',', '.'),
                         product['холестерин'].replace(',', '.'),
                         product['1 ХO є в граммах продукта (Старыи розрах)'].replace(',', '.'),
                         product['1 ХO є в граммах продукта (новий розрах)'].replace(',', '.')))


file = codecs.open('ru_database.json', 'r', 'utf-8-sig')
lines = json.load(file)
file.close()
flourish_food, cereals_food, nut_including, meat, sausages = [], [], [], [], []
sweets, milk_dairy, drinks, cheeses, mushrooms, oysters_crustaceans = [], [], [], [], [], []
potato_included, fruits, pasta_included, fish, eggs = [], [], [], [], []
oil_margarine, vegetables = [],[]
for dic in lines:
    if '1 ХO є в граммах продукта (Старыи розрах)' in dic.keys():
        if int(dic['Номер']) in range(0, 32):
            add_product(flourish_food, dic)
        elif int(dic['Номер']) in range(32, 56):
            add_product(cereals_food, dic)
        elif int(dic['Номер']) in range(55, 81):
            add_product(sweets, dic)
        elif int(dic['Номер']) in range(81, 93):
            add_product(potato_included, dic)
        elif int(dic['Номер']) in range(93, 135):
            add_product(fruits, dic)
        elif int(dic['Номер']) in range(134, 147):
            add_product(pasta_included, dic)
        elif int(dic['Номер']) in range(147, 170):
            add_product(milk_dairy, dic)
        elif int(dic['Номер']) in range(170, 195):
            add_product(drinks, dic)
        elif int(dic['Номер']) in range(195, 207):
            add_product(nut_including, dic)
        elif int(dic['Номер']) in range(207, 234):
            add_product(cheeses, dic)
        elif int(dic['Номер']) in range(234, 260) or int(dic['Номер']) in range(288, 304):
            add_product(meat, dic)
        elif int(dic['Номер']) in range(260, 288):
            add_product(sausages, dic)
        elif int(dic['Номер']) in range(304, 342):
            add_product(fish, dic)
        elif int(dic['Номер']) in range(342, 347):
            add_product(eggs, dic)
        elif int(dic['Номер']) in range(347, 353):
            add_product(mushrooms, dic)
        elif int(dic['Номер']) in range(353, 360):
            add_product(oysters_crustaceans, dic)
        elif int(dic['Номер']) in range(360, 368):
            add_product(oil_margarine, dic)
        elif int(dic['Номер']) in range(360, 368):
            add_product(oil_margarine, dic)
        elif int(dic['Номер']) in range(368, 407):
            add_product(vegetables, dic)
