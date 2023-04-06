#!/usr/local/bin/python3

from gradient_descent import *
import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        x_km = []
        y_price = []
        for row in csvreader:
            x_km.append(row[0])
            y_price.append(row[1])
            # print(', '.join(row))
        x_km.pop(0)
        y_price.pop(0)
    return(x_km, y_price)

def plot_graph(x_km, y_price, y):
    plt.xlabel('X km')
    plt.ylabel('Y price')
    plt.title('XY km/price')
    plt.scatter(x_km, y_price, marker="x")
    plt.scatter(x_km, y, marker="o")
    plt.show()

def plot_cost_function(J):
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost function')
    plt.title('Cost function')
    iterations = list(range(len(J)))
    plt.plot(iterations, J)
    plt.show()

def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list

def normalize_minmax_list(list):
    min_el = min(list)
    max_el = max(list)
    list = [(x_i - min_el)/(max_el - min_el) for x_i in list]
    return list

def normalize_zscore_list(list):
    list_mean = np.mean(list, axis=0)
    list_std = np.std(list, axis=0)
    list_normalized = (list - list_mean) / list_std
    return list_normalized, list_mean, list_std

def main():
    x_km, y_price = read_csv_file('data.csv')
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    x_km = normalize_minmax_list(x_km)
    y_price = normalize_minmax_list(y_price)
    # x_km = normalize_zscore_list(x_km)
    # y_price = normalize_zscore_list(y_price)
    print(x_km)
    print(y_price)
    # theta0, theta1, J = gradient_descent(x_km, y_price, 0, 0, 0.0001, 10000000)
    # theta0, theta1, J = gradient_descent(x_km, y_price, 0, 0, 0.001, 1000000)
    theta0, theta1, J = gradient_descent(x_km, y_price, 0, 0, 0.001, 100000, 0)
    print(len(theta0))
    print(J[-1])
    print(theta0[-1])
    print(theta1[-1])
    # print(type(theta0[-1]))
    y = [theta0[-1] + theta1[-1] * x_i for x_i in x_km]

    plot_graph(x_km, y_price, y)
    plot_cost_function(J)
    # plot_graph(x_km, y)
    
main()
