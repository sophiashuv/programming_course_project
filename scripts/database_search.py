from translate import Translator
import json
import codecs


def get_input():
    """
    (NoneType)-> str
    Take user input and return it translated for futher research.
    """
    translator = Translator(from_lang="ukrainian", to_lang="russian")
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
    file = codecs.open(table_file, 'r', 'utf-8-sig')
    lines = json.load(file)
    file.close()
    for dic in lines:
        for key, value in dic.items():
            if product.upper() in key.upper() or product.upper() in value.upper():
                return dic
