#!/usr/local/bin/python3

from gradient_descent import *
from plot_graph import *
from data_utils import *
from global_vars import *
import subprocess


if __name__ == "__main__":
    # fetch data from csv
    x_km, y_price = read_csv_file('data.csv')
    # train model
    theta, J, y_norm_vars, y_train = train_model(x_km, y_price)
    # create points for the graph
    y_res = create_points(theta, y_norm_vars, x_km)
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

