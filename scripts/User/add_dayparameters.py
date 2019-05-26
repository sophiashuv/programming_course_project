import codecs
from add_user import*
from scripts.json_reading_writing import*


def add_inf(filename):
    """
    The function that adds insulin to the base
    """
    with open(filename, encoding='utf-8') as f:
        f.readline()
        lines = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
        date = str(input("Вкажіть сьогоднішню дату: "))
        time = str(input("Вкажіть поточний час"))
        value = str(input("Вкажіть рівень цукру у крові"))
        a_dict = {"systemTime": date,
                  "eventType": time,
                  "value": value}
        lines['events'].append(a_dict)
        return lines

    
if __name__ == '__main__':
    filename = User().file_name()
    rewrite_json(add_inf(filename), filename)
