from insulin_ADT import Insulin
from flask_glucu.json_reading_writing import*
import json
import codecs


def choice(user_choice):
    """
    The function  that returns True if the user wants to add new insulin and false in case he wants to use the one
    from the base
    """
    if user_choice == "+":
        return True
    else:
        return False


def add_insulin():
    """
    The function that adds insulin to the base
    """
    insulin_name = str(input("Вкажіть  назву інсуліну рекомендованого вашим лікарем-ендокринологом, яку ви "
                             "хочете додати до бази: "))
    with open("table_insulin.json", encoding='utf-8') as f:
        f.readline()
        lines = json.load(codecs.open("table2.json", 'r', 'utf-8-sig'))
        onset = str(input("Вкажіть початок дії вище вказаного вами інсуліну: "))
        peak = str(input("Вкажіть пік дії вище вказаного вами інсуліну: "))
        duration = str(input("Вкажіть тривалість дії вище вказаного вами інсуліну: "))
        a_dict = {'Type of Insulin & Brand Names': insulin_name,
                  'Onset': onset,
                  'Peak': peak,
                  'Duration': duration}
        lines.append(a_dict)
        return lines
    

def find_in_data():
    """
    The function that search insulin in data
    """
    insulin_name = str(input("Вкажіть повну назву інсуліну рекомендованого вашим лікарем-ендокринологом: "))
    with open('table_insulin.json', encoding='utf-8') as f:
        f.readline()
        lines = json.load(codecs.open('table_insulin.json', 'r', 'utf-8-sig'))
        for i in lines:
            if insulin_name in i['Type of Insulin & Brand Names']:
                onset = i['Onset']
                peak = i['Peak']
                duration = i['Duration']
                z = Insulin(insulin_name, onset, peak, duration)
                return z


if __name__ == '__main__':
    choice1 = input("Натисніть +, якщо ви використовуєте інсулін із бази даних, та -, у протилежному випадку: ")
    if choice(choice1):
        rewrite_json(add_insulin(), 'table_insulin.json')
        print("Ви додали рекомендований вам інсулін у базу даних, у подальшому використанні програми ви можете лише"
              " вказувати його назву")
    choice2 = str(input("Якщо ви хочете продовжити натисніть +: "))
    if choice(choice2):
        print(find_in_data())
