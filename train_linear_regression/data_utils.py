import csv
import json
import os
from train_linear_regression.global_vars import *


def save_to_json(theta, y_norm_vars):
    # save theta and y_norm_vars to json file
    data = {}
    data['theta'] = theta
    data['y_norm_vars'] = y_norm_vars
    data['verbosity'] = verbosity
    data['normalization'] = normalization
    data['normalize_y'] = normalize_y
    data['plot_normalize_y'] = plot_normalize_y
    data['alpha'] = alpha
    data['num_iters'] = num_iters
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
        print("[verbosity 2] Directory created at {}".format(res_dir)) if verbosity >= 2 else None
    try:
        with open(res_file, 'w') as outfile:
            json.dump(data, outfile)
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)


def read_csv_file(filename):
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            x_km = []
            y_price = []
            for row in csvreader:
                x_km.append(row[0])
                y_price.append(row[1])
            x_km.pop(0)
            y_price.pop(0)
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)
    return(x_km, y_price)


def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list