#!/usr/local/bin/python3

from predict_price.data_utils import *
from predict_price.model_utils import *
from predict_price.global_vars import *

def main_predict_price():
    mileage_km = input_km()
    theta, y_norm_vars, normalization, normalize_y, plot_normalize_y = read_from_json()
    print("[verbosity 1] theta = {}, y_norm_vars = {}, normalization = {}, normalize_y = {}, plot_normalize_y = {}".format(theta, y_norm_vars, normalization, normalize_y, plot_normalize_y)) if verbosity >= 1 else None
    predict_price = create_function(theta, y_norm_vars, normalization, normalize_y, plot_normalize_y)
    print("Predicted price for {} km: {}".format(mileage_km, predict_price(mileage_km)))

if __name__ == "__main__":
    main_predict_price()