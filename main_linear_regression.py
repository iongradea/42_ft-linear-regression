#!/usr/local/bin/python3

from gradient_descent import *
from plot_graph import *
from data_utils import *
from global_vars import *


def main_linear_regression():
    # fetch data from csv
    x_km, y_price = read_csv_file(data_file)
    # train model
    # note : y_train can be either normalized or not, depending on the value of normalize_y
    theta, J, y_norm_vars, y_train = train_model(x_km, y_price)
    # create points for the graph
    y_res = create_points(theta, y_norm_vars, x_km)
    # create predict_price function
    y_fn = create_function(theta, y_norm_vars)
    # save theta and y_norm_vars to json file
    save_to_json(theta, y_norm_vars)
    # plot graph for y_price/y_train, y_res, y_fn and J
    # we have below the option to either plot the data with y_normalize or without according
    if plot_normalize_y == 'y':
        # if normalize_y option is equal to 'n', plotting normalize is irrelevant because the y data is not normalized
        print("[verbosity 1] normalize_y = {}, plot_normalize_y = {}".format(normalize_y, plot_normalize_y)) if verbosity >= 1 else None
        # y_train is the y data used for training the model and findings thetas
        # if normalize_y is equal to 'y', y_train is normalized
        # that's why plotting y_train, y_res and y_fn together always fit together are these data were used together for training the model
        # plot_graphs(x_km, y_train, y_res, J, y_fn)
    else:
        print("[verbosity 1] normalize_y = {}, plot_normalize_y = {}".format(normalize_y, plot_normalize_y)) if verbosity >= 1 else None
        # y_price is the original y data, never normalized
        # if normalize_y is equal to 'y', y_res is normalized, so we need to unormalize it in order to fit with y_price
        # plot_graphs(x_km, y_price, y_res, J, y_fn)


if __name__ == "__main__":
    main_linear_regression()









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

