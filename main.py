#!/usr/local/bin/python3

from gradient_descent import *
from normalization import *
from plot_graph import *
from data_utils import *

print_level, normalization, alpha, num_iters = program_mode()

def train_model(x_km, y_price):
    global print_level, normalization, alpha, num_iters
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    print("[print level 2] x_km = {}, \ny_price = {}".format(x_km, y_price)) if print_level >= 2 else None
    # normalization
    if normalization == 'm':
        x_km_norm, min_x, max_x = normalize_minmax_list(x_km)
        y_price_norm, min_y, max_y = normalize_minmax_list(y_price)
        print("[print level 2] min_x = {}, max_x = {}, min_y = {}, max_y = {}".format(min_x, max_x, min_y, max_y)) if print_level >= 2 else None
        print("[print level 2] x_km_norm = {}, \ny_price_norm = {}".format(x_km_norm, y_price_norm)) if print_level >= 2 else None
    else:
        x_km_norm, mean_x, std_x = normalize_zscore_list(x_km)
        y_price_norm, mean_y, std_y = normalize_zscore_list(y_price)
        print("[print level 2] mean_x = {}, std_x = {}, mean_y = {}, std_y = {}".format(mean_x, std_x, mean_y, std_y)) if print_level >= 2 else None
        print("[print level 2] x_km_norm = {}, \ny_price_norm = {}".format(x_km_norm, y_price_norm)) if print_level >= 2 else None
    # WIP : gradient descent and J (cost function) with normalized parameters theta0 and theta1 
    theta0, theta1, J = gradient_descent(x_km_norm, y_price_norm, alpha, num_iters)
    print("[print level 1] theta0_normalized = {}, theta1_normalized = {}, J = {}".format(theta0[-1], theta1[-1], J[-1])) if print_level >= 1 else None
    print("[print level 2] len(theta0_normalized) = {} and len(theta1_normalized) = {} and len(J) = {}".format(len(theta0), len(theta1), len(J))) if print_level >= 2 else None

    # WIP : to be plotted outside the function train_model and define y outside 2 for the first part of the exercise
    # result function with the normalized parameters theta0 and theta1
    y = [theta0[-1] + theta1[-1] * x_i for x_i in x_km_norm]
    # plot normalized graph
    plot_graph(x_km_norm, y_price_norm, y)
    # plot cost function normalized
    plot_cost_function(J)
    return theta0[-1], theta1[-1], J # WIP : to be unormalized

if __name__ == "__main__":
    x_km, y_price = read_csv_file('data.csv')
    theta0, theta1, J = train_model(x_km, y_price)
