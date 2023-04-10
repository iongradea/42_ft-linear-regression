import csv
import json
from global_vars import *


def save_to_json(theta, y_norm_vars):
    # save theta and y_norm_vars to json file
    data = {}
    data['theta'] = theta
    data['y_norm_vars'] = y_norm_vars
    data['normalization'] = normalization
    data['normalize_y'] = normalize_y
    data['plot_normalize_y'] = plot_normalize_y
    with open(res_file, 'w') as outfile:
        json.dump(data, outfile)


def read_from_json():
    # read theta and y_norm_vars from json file
    with open(res_file) as json_file:
        data = json.load(json_file)
        # return data
        theta = data['theta']
        y_norm_vars = data['y_norm_vars']
    return theta, y_norm_vars


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