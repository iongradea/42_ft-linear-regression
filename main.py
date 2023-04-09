#!/usr/local/bin/python3

from gradient_descent import *
from normalization import *
from plot_graph import *
from data_utils import *

print_level, normalization, normalize_Y, alpha, num_iters = program_mode()

def train_model(x_km, y_price):
    global print_level, normalization, normalize_Y, alpha, num_iters
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    print("[print level 2] x_km = {}, \ny_price = {}".format(x_km, y_price)) if print_level >= 2 else None

    # normalization
    # note: normalization of y is not mandatory, it can make the process more numerically stable and speed up the convergence
    if normalization == 'm':
        # minmax normalization
        x_km_norm, min_x, max_x = normalize_minmax_list(x_km) 
        if normalize_Y == 'y':
            y_price_norm, min_y, max_y = normalize_minmax_list(y_price)
        else:
            y_price_norm, min_y, max_y = y_price, 0, 0
        print("[print level 2] min_x = {}, max_x = {}".format(min_x, max_x)) if print_level >= 2 else None
        print("[print level 2] min_y = {}, max_y = {}".format(min_y, max_y)) if print_level >= 2 else None
        print("[print level 2] x_km_norm = {}".format(x_km_norm)) if print_level >= 2 else None
        print("[print level 2] normalize_Y = {}, y_price_norm = {}".format(normalize_Y, y_price_norm)) if print_level >= 2 else None
    else:
        # z-score normalization
        x_km_norm, mean_x, std_x = normalize_zscore_list(x_km)
        if normalize_Y == 'y':
            y_price_norm, mean_y, std_y = normalize_zscore_list(y_price)
        else:
            y_price_norm, mean_y, std_y = y_price, 0, 0
        print("[print level 2] mean_x = {}, std_x = {}".format(mean_x, std_x)) if print_level >= 2 else None
        print("[print level 2] mean_y = {}, std_y = {}".format(mean_y, std_y)) if print_level >= 2 else None
        print("[print level 2] x_km_norm = {}".format(x_km_norm)) if print_level >= 2 else None
        print("[print level 2] normalize_Y = {}, y_price_norm = {}".format(normalize_Y, y_price_norm)) if print_level >= 2 else None
    
    # gradient descent and J (cost function) with normalized parameters theta0 and theta1 
    theta0_norm, theta1_norm, J = gradient_descent(x_km_norm, y_price_norm, alpha, num_iters)
    print("[print level 1] theta0_normalized = {}, theta1_normalized = {}, J = {}".format(theta0_norm[-1], theta1_norm[-1], J[-1])) if print_level >= 1 else None
    print("[print level 2] len(theta0_normalized) = {} and len(theta1_normalized) = {} and len(J) = {}".format(len(theta0_norm), len(theta1_norm), len(J))) if print_level >= 2 else None
    
    if normalization == 'm':
        theta0 = theta0_norm[-1] - theta1_norm[-1] * min_x / (max_x - min_x)
        theta1 = theta1_norm[-1] / (max_x - min_x)
    else:
        theta0 = theta0_norm[-1] - theta1_norm[-1] * mean_x / std_x
        theta1 = theta1_norm[-1] / std_x
    
    # if normalize_Y == 'y':
    #     if normalization == 'm':
    #         y_res = [theta0 + theta1 * x_i for x_i in x_km]
    #     else:
    #         y_res = [(theta0 + theta1 * x_i)  for x_i in x_km]
    # else:
    #     y_res = [theta0 + theta1 * x_i for x_i in x_km]
    
    return theta0, theta1, J, y_price_norm, std_y, mean_y

if __name__ == "__main__":
    x_km, y_price = read_csv_file('data.csv')
    theta0, theta1, J, y_price_norm, std_y, mean_y = train_model(x_km, y_price)
    y_res = [(theta0 + theta1 * x_i) * std_y + mean_y for x_i in x_km]
    y_res_norm = [theta0 + theta1 * x_i for x_i in x_km]
    plot_graph(x_km, y_price, y_res)
    plot_graph(x_km, y_price_norm, y_res_norm)
    plot_cost_function(J)
