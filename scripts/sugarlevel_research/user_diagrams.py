import json
import codecs
import numpy as np
import matplotlib.pyplot as plt


def file_name(login):
    """
    returns a file name
    """
    if " " in login:
        login = login.replace(" ", "")
    return str(login).lower() + '.json'


def user_json(login):
    """
    returns the contents of json
    """
    return (json.load(codecs.open(file_name(login), 'r', 'utf-8-sig')))["events"]


def parameters(date, lines):
    """
    The function that returns lists of sugar levels, time and a date
    """
    height = []
    bars = []
    for i in lines['events']:
        if i['date'] == date:
            height.append(float(i['value']))
            bars.append(i['time'])
    return height, bars, date


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
    plt.savefig('daydiagram.png')
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
    plt.savefig('weekdiagram.png')
    plt.close()


if __name__ == "__main__":
    daily_diagram("name_surname.json")
    weekly_diagram("name_surname.json")
