from json_reading_writing import*
from database_search import*
import numpy as np
import matplotlib.pyplot as plt

def search_user(login):
    """
    The function that returns all information about user
    """
    for i in file_read("user.json")["user_name"]:
        if i["login"] == login:
            return i

def insulin_dose(login, sugar_level):
    """
    (str, str) -> float
    The function that returns an ordinary insulin dose before a meal
    """
    return (float(search_user(login)['normal_level_of_shugar']) + (float(sugar_level)-7)/2)

def food_preferenses(login, product, food_amount):
    """
    The function that returns a list of doses of XO eaten and not
    """
    products = product.split(",")
    print(products)
    food_amounts = food_amount.split(",")
    eaten = 0
    available = float(search_user(login)['XO'])
    for num_of_food in range(len(products)):
        gramm_in_xo = float(found_in_database("ru_bread_items.json", products[num_of_food])["1 ХO є в граммах продукта (новий розрах)"])
        eaten += float(food_amounts[num_of_food])/gramm_in_xo
    available -= eaten
    return[available, eaten]

def diadram_xo(login, product, food_amount):
    sizes = food_preferenses(login, product, food_amount)
    date1 = "Залишилось"
    date2 = "Спожите"

    labels = [date1, date2]
    colors = ['#a0e88f', '#e88f95']
    explode = (0.05, 0.15)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=200)

    plt.axis('equal')
    plt.xlabel("Діаграма, що ілюструє відсоток\nспожитих за день хлібних одиниць від добової норми",
               fontweight='bold', color='#44af83', style = 'oblique')
    plt.show()


print(food_preferenses("jbrown", "Йогурт, йогурт", "100, 100"))
print(insulin_dose("jbrown","9"))
diadram_xo("jbrown", "Йогурт", "0")