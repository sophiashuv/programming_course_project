from translate import Translator
import json
import codecs
translator = Translator(from_lang="ukrainian", to_lang="russian")


def get_input():
    """
    (NoneType)-> str
    Take user input and return it translated for futher research.
    """
    user_input = input('Введіть назву спожитого продукту: ')
    translation = translator.translate(user_input)

    for y in translation:
        if not y.isalpha() and y not in user_input:
            translation = translation.replace(y, '')
    return translation


def found_in_database(table_file, product):
    """
    (str,str)->dict
    Take file and name of product, find product description in file and return it.
    """
    with open(table_file, encoding='utf-8') as f:
        file = codecs.open(table_file, 'r', 'utf-8-sig')
        lines = json.load(file)
        file.close()
    for dic in lines:
        for key, value in dic.items():
            if product.upper() in key.upper() or product.upper() in value.upper():
                return dic


if __name__ == '__main__':
    product_name = get_input()
    print(found_in_database('ru_bread_items.json', product_name)) 
