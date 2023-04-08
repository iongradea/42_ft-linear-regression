#!/usr/local/bin/python3

from gradient_descent import *
from normalization import *
from plot_graph import *
from data_utils import *

def main():
    x_km, y_price = read_csv_file('data.csv')
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    x_km_norm, _, _ = normalize_minmax_list(x_km)
    y_price_norm, _, _ = normalize_minmax_list(y_price)
    print("x_km_norm : {}".format(x_km_norm))
    print("y_price_norm : {}".format(y_price_norm))
    print("y_price : {}".format(y_price))
    print(type(x_km_norm))
    # x_km_norm, _, _ = normalize_zscore_list(x_km)
    # y_price_norm, _, _ = normalize_zscore_list(y_price)
    # print("x_km_norm : {}".format(x_km_norm))
    # print("y_price_norm : {}".format(y_price_norm))
    # print("y_price : {}".format(y_price))
    # print(type(x_km_norm))
    # theta0, theta1, J = gradient_descent(x_km, y_price, 0.0001, 10000000)
    # theta0, theta1, J = gradient_descent(x_km, y_price, 0.001, 1000000)
    # theta0, theta1, J = gradient_descent(x_km, y_price, 0.001, 100000, 0)
    theta0, theta1, J = gradient_descent(x_km_norm, y_price_norm, 0.1, 1000)
    print("len(theta0) : {}".format(len(theta0)))
    print("J[-1] : {}".format(J[-1]))
    print("theta0[-1] : {}".format(theta0[-1]))
    print("theta1[-1] : {}".format(theta1[-1]))
    print("type(theta0[-1]) : {}".format(type(theta0[-1])))
    y = [theta0[-1] + theta1[-1] * x_i for x_i in x_km_norm]
    print("y_price : {}".format(y_price))
    print("y : {}".format(y))
    print("x_km : {}".format(x_km))

    plot_graph(x_km_norm, y_price_norm, y)
    plot_cost_function(J)
    # plot_graph(x_km, y)
    
main()
