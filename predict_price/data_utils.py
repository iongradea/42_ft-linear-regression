import json
import argparse
from predict_price.global_vars import *


def program_mode():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Getting command line options")

    # Add command-line options
    parser.add_argument("-v", "--verbose", type=int, choices=[0, 1], default=1, help="Enter the verbosity level : 0 (no print), 1 (basc info)")

    # Parse the command-line options
    args = parser.parse_args()

    return args.verbose


verbosity = program_mode()


def input_km():
    # get user input
    try:
        km = int(input("Enter the kilometers: "))
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)
    return km


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