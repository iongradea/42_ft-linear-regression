import csv
from global_vars import *

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


def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        x_km = []
        y_price = []
        for row in csvreader:
            x_km.append(row[0])
            y_price.append(row[1])
        x_km.pop(0)
        y_price.pop(0)
    return(x_km, y_price)


def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list