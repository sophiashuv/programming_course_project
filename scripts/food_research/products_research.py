from sort_database import *
import matplotlib as mpl
import matplotlib.pyplot as plt


def sort_by_fats(block):
    """
    :param block: list
    Creates a diagram base on fats rating
    """
    values_names = sorted([(products.get_fats(), products.name) for products in block])
    data_names = [item[0] for item in values_names]
    data_values = [item[1] for item in values_names]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1500 / dpi, 800 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.title('Fat content rating ')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)

    xs = range(len(data_names))
    plt.bar([x + 0.3 for x in xs], data_values,
            width=0.4, color='dimgrey', alpha=0.7, label='rating of fat',
            zorder=2)
    plt.xticks(xs, data_names)

    fig.autofmt_xdate(rotation=25)

    plt.legend(loc='upper right')
    fig.savefig('fish_fat.png')


def sort_by_bread_items(block):
    """
    :param block: list
    Creates a diagram base on bread items rating
    """
    values_names = sorted([(products.count_value('bread items', 100), products.name) for products in block])
    data_names = [item[0] for item in values_names]
    data_values = [item[1] for item in values_names]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1500 / dpi, 800 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.title('Bread items content rating ')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)

    xs = range(len(data_names))
    plt.bar([x + 0.3 for x in xs], data_values,
            width=0.4, color='dimgrey', alpha=0.7, label='rating of bread item content in 100gr',
            zorder=2)
    plt.xticks(xs, data_names)

    fig.autofmt_xdate(rotation=25)

    plt.legend(loc='upper right')
    fig.savefig('bread_items_fish.png')

def sort_by_cholesterol(block):
    """
    :param block: list
    Creates a diagram base on cholesterol rating
    """
    values_names = sorted([(products.get_cholesterol(), products.name) for products in block])
    data_names = [item[0] for item in values_names]
    data_values = [item[1] for item in values_names]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1500 / dpi, 800 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.title('Cholesterol content rating ')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)

    xs = range(len(data_names))
    plt.bar([x + 0.3 for x in xs], data_values,
            width=0.4, color='purple', alpha=0.7, label='rating of cholesterol',
            zorder=2)
    plt.xticks(xs, data_names)

    fig.autofmt_xdate(rotation=25)

    plt.legend(loc='upper right')
    fig.savefig('fish_cholesterol.png')


if __name__ == '__main__':
    sort_by_fats(fish)
    sort_by_fats(sweets)
    sort_by_fats(cheeses)

    sort_by_bread_items(fish)
    sort_by_bread_items(sweets)
    sort_by_bread_items(cheeses)


