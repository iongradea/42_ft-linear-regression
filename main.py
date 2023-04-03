#!/usr/local/bin/python3

from gradient_descent import *
import csv
import matplotlib.pyplot as plt

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
    plt.scatter(x_km, y_price)
    plt.scatter(x_km, y)
    plt.show()

def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list

def main():
    x_km, y_price = read_csv_file('data.csv')
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    theta0, theta1, J = gradient_descent(x_km, y_price, 0, 0, 0.0000000001, 1000000)
    print(len(theta0))
    print(J[-1])
    print(theta1[-1])
    print(type(theta0[-1]))
    y = [theta0[-1] - theta1[-1] * x_i for x_i in x_km]
    plot_graph(x_km, y_price, y)
    # plot_graph(x_km, y)
    
main()
