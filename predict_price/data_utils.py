import json
import os
from predict_price.global_vars import *


def read_from_json():
    # read theta and y_norm_vars from json file
    try:
        with open(res_file) as json_file:
            data = json.load(json_file)
            # return data
            theta = data['theta']
            y_norm_vars = data['y_norm_vars']
            normalization = data['normalization']
            normalize_y = data['normalize_y']
            plot_normalize_y = data['plot_normalize_y']
    except Exception as e: 
        print("Error: {}".format(e))
        print("Please train the model first.")
        exit(1)
    return theta, y_norm_vars, normalization, normalize_y, plot_normalize_y