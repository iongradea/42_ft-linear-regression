#!/usr/local/bin/python3

from predict_price.data_utils import *
from predict_price.model_utils import *
from predict_price.global_vars import *

def main_predict_price():
    theta, y_norm_vars, normalization, normalize_y, plot_normalize_y = read_from_json()
    predict_price = create_function(theta, y_norm_vars, normalization, normalize_y, plot_normalize_y)
    print("Predicted price for 45000 km: {}".format(predict_price(45000)))

if __name__ == "__main__":
    main_predict_price()