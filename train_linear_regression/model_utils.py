import numpy as np
from train_linear_regression.global_vars import *

# function to create points for the graph
def create_points(theta, y_norm_vars, x_km):
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


def create_function(theta, y_norm_vars):
    # assign values
    [theta0, theta1] = theta 
    [min_y, max_y, std_y, mean_y] = y_norm_vars

    # unormalize y if necessary
    if normalize_y == 'y':
        if plot_normalize_y == 'y':
            predict_price = lambda x: theta0 + theta1 * x
        else:
            if normalization == 'm':
                predict_price = lambda x: (theta0 + theta1 * x) * (max_y - min_y) + min_y
            else:
                predict_price = lambda x: (theta0 + theta1 * x) * std_y + mean_y
    else:
        predict_price = lambda x: theta0 + theta1 * x
    return predict_price


def normalize_minmax_list(list):
    min_el = min(list)
    max_el = max(list)
    list_normalized = [(x_i - min_el)/(max_el - min_el) for x_i in list]
    return list_normalized, min_el, max_el


def normalize_zscore_list(list):
    list_mean = np.mean(list, axis=0)
    list_std = np.std(list, axis=0)
    list_normalized = (list - list_mean) / list_std
    return list_normalized, list_mean, list_std