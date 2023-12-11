# -*- coding: utf-8 -*-

"""
Функции, необходимые для работы над базой данных и проектом.

"""
import pandas as pd
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from math import isnan

os.chdir(r'../Data/')

def checkihgStringOrFloat(data):
    """
    Проверка параметра, полученного на вход, на строку или число с плавающей точкой.

    Параметры:
    data - параметр, который проверяется с помощью данной функции

    :return:
    float(data): параметр в виде числа с плавающей точкой, которое используется в дальнейшем.
    or
    str(data): параметр в виде строки, которое используется в дальнейшем.
    """
    try:
        return float(data)
    except ValueError:
        return str(data)


def checkingStringOrInt(data):
    """
    Проверка параметра, полученного на вход, на строку или целое число.

    Параметры:
    data - параметр, который проверяется с помощью данной функции

    :return:
    int(data): параметр в виде целого числа, которое используется в дальнейшем.
    or
    str(data): параметр в виде строки, которое используется в дальнейшем.
    """
    try:
        return int(data)
    except ValueError:
        return str(data)


def barAndPieGraph():
    """
    Получение двух графиков: столбчатый и круговой на основе таблиц: РостМужчинИЖенщин.csv и Код.csv
    Параметры:

    :return:
    Два графика:
    Столбчатый график "Средний рост на разных континентах" с осями:
            Ось абцисс: Континент
            Ось ординат: Средний рост на данном континенте
    Круговой график "Процент представителей с разных континентов" с осями:
            Ось абцисс: Континент
            Ось ординат: Процент прдеставителей
    """
    secondDataBase = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
    thirdDataBase = pd.read_csv('Код.csv', delimiter=';')

    CodeContinent = np.array(thirdDataBase)
    HeightManAndWoman = np.array(secondDataBase)

    codes = CodeContinent[0:, 0]
    continents = CodeContinent[0:, 2]
    manHeight = HeightManAndWoman[0:, 1]
    dictionary = dict()

    for continent in continents:
        dictionary[continent] = list()
    for code, height, continent in zip(codes, manHeight, continents):
        dictionary[continent].append(height)

    for i in dictionary:
        dictionary[i] = len(dictionary[i])
    clean_dict = {k: dictionary[k] for k in dictionary if type(k) == str}
    keys = clean_dict.keys()
    values = clean_dict.values()
    explode = (0.1, 0, 0.15, 0, 0.2, 0)

    fig, ax = plt.subplots()
    plt.bar(keys, values, color='g', width=0.5)
    fig.autofmt_xdate()
    plt.title("Mean height in different continents")
    plt.gca().set(xlabel='Continent', ylabel='Height')

    fig, ax = plt.subplots()
    explode = (0, 0.1, 0.1, 0, 0, 0)
    plt.title("Percentage of representatives from different continents ")
    ax.pie(values, labels=keys,
           autopct='%.3f%%',
           shadow=True,
           explode=explode,
           wedgeprops={'lw': 0.5, 'ls': '--', 'edgecolor': "k"},
           rotatelabels=False,
           )
    ax.axis("Equal")
    plt.show()


barAndPieGraph()