#!/usr/local/bin/python3

from predict_price.data_utils import *
from predict_price.model_utils import *
from predict_price.global_vars import *

def main_predict_price():
    theta, y_norm_vars, normalization, normalize_y, plot_normalize_y, alpha, num_iters = read_from_json()
    mileage_km = input_km()
    theta0, theta1 = theta
    min_y, max_y, std_y, mean_y = y_norm_vars
    print("[verbosity 1] theta0 = {}, theta1 = {}".format(theta0, theta1)) if verbosity >= 1 else None
    print("[verbosity 1] alpha = {}, num_iters = {}".format(alpha, num_iters)) if verbosity >= 1 else None
    print("[verbosity 1] min_y = {}, max_y = {}, std_y = {}, mean_y = {}".format(min_y, max_y, std_y, mean_y)) if verbosity >= 1 else None
    print("[verbosity 1] normalization = {}, normalize_y = {}, plot_normalize_y = {}".format(normalization, normalize_y, plot_normalize_y)) if verbosity >= 1 else None
    predict_price = create_function(theta, y_norm_vars, normalization, normalize_y, plot_normalize_y)
    print("Predicted price for {} km: {:.2f} euros".format(mileage_km, predict_price(mileage_km)))

if __name__ == "__main__":
    main_predict_price()