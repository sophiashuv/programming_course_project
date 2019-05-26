import json
import codecs
import numpy as np
import matplotlib.pyplot as plt


def read_file(filename):
    """
    The function that reads json file
    """
    file = codecs.open(filename, 'r', 'utf-8-sig')
    lines = json.load(file)
    file.close()
    return lines


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


def count_mid(lines):
    """
    The funcrion tat counts medium level of sugar of a day and returns a list of medium levels of sugar for
    the last 7 days and list od dates
    """
    n = -1
    lst_sug = []
    lst_date = []
    while n != -36:
        height, bars, date = parameters(lines['events'][n]['date'], lines)
        mid = sum(height)/len(height)
        n -= 5
        lst_sug.append(mid)
        lst_date.append(date)
    return lst_sug, lst_date


def d1(height, bars, date):
    """
    The function that builds a Stacked Barplot
    """
    barWidth = 0.25
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color='#EB984E', width=barWidth, edgecolor='white', label='var1')
    plt.xticks(y_pos, bars, color='#873600')
    plt.yticks(color='#873600')
    plt.xlabel(date, fontweight='bold', color='#D35400')
    plt.show()


def d2(size, names):
    """
    The function that builds a Pie plot
    """
    np = []
    for i in range(7):
        np.append((str(round(size[i], 2)) + "\n"+names[i]))
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    plt.rcParams['text.color'] = 'black'
    my_circle = plt.Circle((0, 0), 0.01, color='white')
    col = ['#A9CCE3', '#AED6F1', '#85C1E9', '#5499C7', '#2471A3', '#1F618D', '#154360']
    plt.pie(size, labels=np, colors=col, shadow=True, startangle=140)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()


if __name__ == "__main__":
    height, bars, date = parameters("11.05.19", read_file("name_surname.json"))
    d1(height, bars, date)
    size, names = count_mid(read_file("name_surname.json"))
    d2(size, names)


