from flasc_glucu.database_search import found_in_database
from  product_ADT import Product
if __name__ == '__main__':

    baguet = found_in_database('ru_bread_items.json', 'багет')
    product = Product(baguet['Номер'], baguet['Продукт'], baguet['ккал'].replace(',', '.'),
                      baguet['білок'].replace(',', '.'), baguet['жири'].replace(',', '.'), baguet['вуглеводи'].replace(',', '.'),
                      baguet['холестерин'].replace(',', '.'), baguet['1 ХO є в граммах продукта (Старыи розрах)'].replace(',', '.'),
                      baguet['1 ХO є в граммах продукта (новий розрах)'].replace(',', '.'))
    print(str(product), '\n')
    product.count_value('protein', 300)
    product.count_value('ccal', 300)
    product.count_value('bread items', 300)
    product.count_value('carbohydrates', 300)
    product.count_value('cholesterol', 300)
