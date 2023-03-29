#!/usr/local/bin/python3
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

def plot_graph(x_km, y_price):
    plt.xlabel('X km')
    plt.ylabel('Y price')
    plt.title('XY km/price')
    plt.scatter(x_km, y_price)
    plt.show()


def main():
    x_km, y_price = read_csv_file('data.csv')
    plot_graph(x_km, y_price)
    
main()
