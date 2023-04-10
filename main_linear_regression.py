#!/usr/local/bin/python3

from gradient_descent import *
from normalization import *
from plot_graph import *
from data_utils import *
import subprocess

verbosity, normalization, normalize_y, plot_normalize_y, alpha, num_iters = program_mode()

# train linear regression model
def train_model(x_km, y_price):
    global verbosity, normalization, normalize_y, alpha, num_iters
    min_y, max_y, mean_y, std_y = 0, 0, 0, 0
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    print("[verbosity 2] x_km = {}, \ny_price = {}".format(x_km, y_price)) if verbosity >= 2 else None

    # normalization
    # note: normalization of y is not mandatory, it can make the process more numerically stable and speed up the convergence
    if normalization == 'm':
        # minmax normalization
        x_train_norm, min_x, max_x = normalize_minmax_list(x_km) 
        if normalize_y == 'y':
            y_train, min_y, max_y = normalize_minmax_list(y_price)
        else:
            y_train, min_y, max_y = y_price, 0, 0
        print("[verbosity 2] min_x = {}, max_x = {}".format(min_x, max_x)) if verbosity >= 2 else None
        print("[verbosity 2] min_y = {}, max_y = {}".format(min_y, max_y)) if verbosity >= 2 else None
        print("[verbosity 2] x_train_norm = {}".format(x_train_norm)) if verbosity >= 2 else None
        print("[verbosity 2] normalize_y = {}, y_train = {}".format(normalize_y, y_train)) if verbosity >= 2 else None
    else:
        # z-score normalization
        x_train_norm, mean_x, std_x = normalize_zscore_list(x_km)
        if normalize_y == 'y':
            y_train, mean_y, std_y = normalize_zscore_list(y_price)
        else:
            y_train, mean_y, std_y = y_price, 0, 0
        print("[verbosity 2] mean_x = {}, std_x = {}".format(mean_x, std_x)) if verbosity >= 2 else None
        print("[verbosity 2] mean_y = {}, std_y = {}".format(mean_y, std_y)) if verbosity >= 2 else None
        print("[verbosity 2] x_train_norm = {}".format(x_train_norm)) if verbosity >= 2 else None
        print("[verbosity 2] normalize_y = {}, y_train = {}".format(normalize_y, y_train)) if verbosity >= 2 else None
    
    # gradient descent and J (cost function) with normalized parameters theta0 and theta1 
    theta0_norm, theta1_norm, J = gradient_descent(x_train_norm, y_train, alpha, num_iters)
    print("[verbosity 1] theta0_normalized = {}, theta1_normalized = {}, J = {}".format(theta0_norm[-1], theta1_norm[-1], J[-1])) if verbosity >= 1 else None
    print("[verbosity 2] len(theta0_normalized) = {} and len(theta1_normalized) = {} and len(J) = {}".format(len(theta0_norm), len(theta1_norm), len(J))) if verbosity >= 2 else None
    
    # unormalize theta0 and theta1
    if normalization == 'm':
        theta0_res = theta0_norm[-1] - theta1_norm[-1] * min_x / (max_x - min_x)
        theta1_res = theta1_norm[-1] / (max_x - min_x)
    else:
        theta0_res = theta0_norm[-1] - theta1_norm[-1] * mean_x / std_x
        theta1_res = theta1_norm[-1] / std_x

    # return results
    theta_res = [theta0_res, theta1_res]
    y_norm_vars = [min_y, max_y, std_y, mean_y]
    
    return theta_res, J, y_norm_vars, y_train

# function to create points for the graph
def create_points(theta, y_norm_vars):
    # assign values
    [theta0, theta1] = theta 
    [min_y, max_y, std_y, mean_y] = y_norm_vars

    # unormalize y if necessary
    if normalize_y == 'y':
        if plot_normalize_y == 'y':
            y_res = [theta0 + theta1 * x_i for x_i in x_km]
        else:
            if normalization == 'm':
                y_res = [(theta0 + theta1 * x_i) * (max_y - min_y) + min_y for x_i in x_km]
            else:
                y_res = [(theta0 + theta1 * x_i) * std_y + mean_y for x_i in x_km]
    else:
        y_res = [theta0 + theta1 * x_i for x_i in x_km]
    return y_res


if __name__ == "__main__":
    # fetch data from csv
    x_km, y_price = read_csv_file('data.csv')
    # train model
    theta, J, y_norm_vars, y_train = train_model(x_km, y_price)
    # create points for the graph
    y_res = create_points(theta, y_norm_vars)
    # plot graph
    if plot_normalize_y == 'y':
        # if normalize_y option is equal to 'n', plotting normalize is irrelevant because the y data is not normalized
        print("[verbosity 1] normalize_y = {}, plot_normalize_y = {}".format(normalize_y, plot_normalize_y)) if verbosity >= 1 else None
        # y_train is the y data used for training the model and findings thetas
        plot_graph(x_km, y_train, y_res)
    else:
        print("[verbosity 1] normalize_y = {}, plot_normalize_y = {}".format(normalize_y, plot_normalize_y)) if verbosity >= 1 else None
        # y_price is the original y data
        plot_graph(x_km, y_price, y_res)
    plot_cost_function(J)
    # subprocess.run(["python3", "main_predict_price.py", str(1)])









    # create predict_price function 
    # predict_price = create_function(theta, y_norm_vars)









# def create_function(theta, y_norm_vars):
#     # assign values
#     [theta0, theta1] = theta 
#     [min_y, max_y, std_y, mean_y] = y_norm_vars

#     # unormalize y if necessary
#     if normalize_y == 'y':
#         if normalization == 'm':
#             predict_price = lambda x: (theta0 + theta1 * x) * (max_y - min_y) + min_y
#         else:
#             predict_price = lambda x: (theta0 + theta1 * x) * std_y + mean_y
#     else:
#         predict_price = lambda x: theta0 + theta1 * x
#     return predict_price

