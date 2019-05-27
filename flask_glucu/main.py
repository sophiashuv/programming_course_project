from flask_glucu.database_search import*
import matplotlib.patheffects as path_effects
from flask_glucu.add import *
import matplotlib.pyplot as plt
import numpy as np


def search_user(login):
    """
    Returns all information about user
    """
    with open("user.json", encoding='utf-8') as f:
        f.readline()
        lines = (json.load(codecs.open("user.json", 'r', 'utf-8-sig')))["user_name"]
    for user in lines:
        if user['login'] == login:
            return user


def check_login(login, password):
    """
    Returns all information about user
    """
    with open('user.json',  encoding='utf-8') as f:
        d = json.load(f)
    for x in d['user_name']:
        if x['login'] == str(login) and x['password'] == str(password):
            return True
        else:
            continue
    return False


def insulin_dose(login, sugar_level):
    """
    Returns an ordinary insulin dose before a meal
    """
    return float(search_user(login)['normal_level_of_shugar']) + (float(sugar_level)-7)/2


def user_json(login):
    return (json.load(codecs.open(file_name(login), 'r', 'utf-8-sig')))["events"]


def food_preferenses(login, product, food_amount, date):
    """
    Returns a list of doses of XO consumed and still available
    """
    eaten = 0
    user_file = user_json(login)
    for event in user_file:
        try:
            if event['date'] == date:
                eaten += event['consumed']
        except IndexError:
            continue

    products = product.split(",")
    food_amounts = food_amount.split(",")
    for num_of_food in range(len(products)):
        gramm_in_xo = float(found_in_database("ru_bread_items.json".replace(',', '.'),
                                              products[num_of_food])["1 ХO є в граммах продукта"
                                                                     " (новий розрах)"].replace(',', '.'))
        eaten += round(float(food_amounts[num_of_food])/gramm_in_xo, 2)
    available = float(search_user(login)['XO'].replace(',', '.')) - eaten
    return[available, eaten]


def diadram_xo(login, product, food_amount, date):
    """
    Builds diagram for percentage of food consumed
    """
    sizes = food_preferenses(login, product, food_amount, date)
    date1 = "Залишилось:" + "\n" + str(sizes[0]) + " ХО."
    date2 = "Спожите:" + "\n" + str(sizes[1]) + " ХО."
    labels = [date1, date2]
    colors = ['#a0e88f', '#e88f95']
    explode = (0.05, 0.15)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=200)
    plt.axis('equal')
    plt.xlabel("Діаграма, що ілюструє відсоток\nспожитих за день хлібних одиниць від добової норми",
               fontweight='bold', color='#44af83', style='oblique')
    plt.savefig('static/images/food_percents.png')
    plt.close()


def insulin_dose_picture(login, sugar_level):
    """
    Makes a picture with a dose of insulin for user
    """
    fig = plt.figure(figsize=(5, 1.5))
    text = fig.text(0.5, 0.5, (str(insulin_dose(login, sugar_level)) + "\nодиниць інсуліну"),
                    ha='center', va='center', style='italic',  size=40, color='#669ea0')
    text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='#446466'),
                           path_effects.Normal()])
    plt.savefig('static/images/dose.png')
    plt.close(fig)


def count_mid(date, login):
    """
    Returns medium value of sugal level of a day
    """
    lst_doz = []
    user_file = user_json(login)
    for day in user_file:
        if day['date'] == date:
            lst_doz.append(round(float(day["value"]), 2))
    return sum(lst_doz)/len(lst_doz)


def count_mid_week(login):
    """
    Counts medium level of sugar of a day and returns a list of medium levels of sugar for
    the last 7 days and list od dates
    """
    user_file = user_json(login)
    lst_dozes = []
    lst_dates = []
    for i in user_file:
        if i['date'] not in lst_dates:
            lst_dates.append(i['date'])
    for i in lst_dates[-7:]:
        lst_dozes.append(count_mid(i, login))
    return lst_dozes,  lst_dates[-7:]


def day(login):
    """
    Returns lists of heights and bars needed for a diagram and a day
    """
    height, bars = [], []
    user_file = (json.load(codecs.open(file_name(login), 'r', 'utf-8-sig')))["events"]
    for days in user_file:
        if days["date"] == user_file[-1]["date"]:
            height.append(float(days["value"]))
            bars. append(days["time"])
    return height, bars, user_file[-1]["date"]


def daily_diagram(login):
    """
    Builds a diagram of daily level of sugar
    """
    height, bars, date = day(login)
    barWidth = 0.25
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color='#EB984E', width=barWidth, edgecolor='white', label='var1')
    plt.xticks(y_pos, bars, color='#873600')
    plt.yticks(color='#873600')
    plt.xlabel(date, fontweight='bold', color='#D35400')
    plt.savefig('static/images/daily.png')
    plt.close()


def weekly_diagram(login):
    """
    Builds a diagram of weekle sugar level values
    """
    size, names = count_mid_week(login)
    np = []
    for i in range(min(7, len(size))):
        np.append((str(round(size[i], 2)) + "\n"+names[i]))
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    plt.rcParams['text.color'] = 'black'
    my_circle = plt.Circle((0, 0), 0.01, color='white')
    col = ['#A9CCE3', '#AED6F1', '#85C1E9', '#5499C7', '#2471A3', '#1F618D', '#154360']
    plt.pie(size, labels=np, colors=col, shadow=True, startangle=140)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('static/images/weekly.png')
    plt.close()

