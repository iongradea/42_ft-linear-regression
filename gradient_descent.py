from normalization import *
from data_utils import *
from global_vars import *

# train linear regression model
def train_model(x_km, y_price):
    global verbosity, normalization, normalize_y, alpha, num_iters
    min_y, max_y, mean_y, std_y = 0, 0, 0, 0
    x_km = convert_list_to_float(x_km)
    y_price = convert_list_to_float(y_price)
    print("[verbosity 2] x_km = {}, \ny_price = {}".format(x_km, y_price)) if verbosity >= 2 else None

    # normalization
    # note: normalization of y is not mandatory, it can make the process more numerically stable and speed up the convergence
    if normalization == 'm':
        # minmax normalization
        x_train_norm, min_x, max_x = normalize_minmax_list(x_km) 
        if normalize_y == 'y':
            y_train, min_y, max_y = normalize_minmax_list(y_price)
        else:
            y_train, min_y, max_y = y_price, 0, 0
        print("[verbosity 2] min_x = {}, max_x = {}".format(min_x, max_x)) if verbosity >= 2 else None
        print("[verbosity 2] min_y = {}, max_y = {}".format(min_y, max_y)) if verbosity >= 2 else None
        print("[verbosity 2] x_train_norm = {}".format(x_train_norm)) if verbosity >= 2 else None
        print("[verbosity 2] normalize_y = {}, y_train = {}".format(normalize_y, y_train)) if verbosity >= 2 else None
    else:
        # z-score normalization
        x_train_norm, mean_x, std_x = normalize_zscore_list(x_km)
        if normalize_y == 'y':
            y_train, mean_y, std_y = normalize_zscore_list(y_price)
        else:
            y_train, mean_y, std_y = y_price, 0, 0
        print("[verbosity 2] mean_x = {}, std_x = {}".format(mean_x, std_x)) if verbosity >= 2 else None
        print("[verbosity 2] mean_y = {}, std_y = {}".format(mean_y, std_y)) if verbosity >= 2 else None
        print("[verbosity 2] x_train_norm = {}".format(x_train_norm)) if verbosity >= 2 else None
        print("[verbosity 2] normalize_y = {}, y_train = {}".format(normalize_y, y_train)) if verbosity >= 2 else None
    
    # gradient descent and J (cost function) with normalized parameters theta0 and theta1 
    theta0_norm, theta1_norm, J = gradient_descent(x_train_norm, y_train, alpha, num_iters)
    print("[verbosity 1] theta0_normalized = {}, theta1_normalized = {}, J = {}".format(theta0_norm[-1], theta1_norm[-1], J[-1])) if verbosity >= 1 else None
    print("[verbosity 2] len(theta0_normalized) = {} and len(theta1_normalized) = {} and len(J) = {}".format(len(theta0_norm), len(theta1_norm), len(J))) if verbosity >= 2 else None
    
    # unormalize theta0 and theta1
    if normalization == 'm':
        theta0_res = theta0_norm[-1] - theta1_norm[-1] * min_x / (max_x - min_x)
        theta1_res = theta1_norm[-1] / (max_x - min_x)
    else:
        theta0_res = theta0_norm[-1] - theta1_norm[-1] * mean_x / std_x
        theta1_res = theta1_norm[-1] / std_x

    # return results
    theta_res = [theta0_res, theta1_res]
    y_norm_vars = [min_y, max_y, std_y, mean_y]
    
    return theta_res, J, y_norm_vars, y_train


# Concept of gradient descent in linear regression ...
#
# the cost J :
# J = 1/2m * sum(h(x) - y)^2 with h(x) = theta0 + theta1 * x 
# Meaning of the cost function in math : The minimum distance between the points (x, y) and the hypothesis (x, h(x))
# The goal is to minimize the cost function J
#
# The gradient descent algorithm :
# thetaj = thetaj - alpha * 1/m * sum(h(x) - y) 
# j are the parameters of the hypothesis from j = 0 to n, in our case j = 0 and j = 1
# The sum is on all the training examples from i = 0 to m
# Meaning of algorith in math : thetaj = thetaj - alpha * dJ / dthetaj
#
# Source : https://www.simplilearn.com/tutorials/machine-learning-tutorial/cost-function-in-machine-learning
# 
# Python notes :
# list theta0[-1] accesses the last element, theta0[-1] therefore equals theta0[el]
#
def gradient_descent(x, y, alpha, num_iters):
    m = len(y)  # number of training examples

    # Initialize theta0 and theta1 as lists with the initial values
    theta0 = [0]
    theta1 = [0]
    J = []  # cost function initialization

    # for each iteration, we compute the hypothesis, the error, the new theta0 and theta1 and the new cost function J
    for el in range(num_iters): # el is ignored in the loop, we use -1 to access the last element
        # we compute for all the training examples for i = 1 to m
        h = [theta0[-1] + theta1[-1] * x_i for x_i in x]  # hypothesis
        error = [h_i - y_i for h_i, y_i in zip(h, y)]  # prediction error

        tmptheta0 = alpha / m * sum(error)  # step for theta0 : (alpha / m) * dJ / dtheta0
        tmptheta1 = alpha / m * sum(e_i * x_i for e_i, x_i in zip(error, x))  # tep for theta1 : (alpha / m) * dJ / dtheta1

        theta0.append(theta0[-1] - tmptheta0) # gradient descent for theta0
        theta1.append(theta1[-1] - tmptheta1) # gradient descent for theta1

        J.append(1 / (2 * m) * sum(e_i ** 2 for e_i in error)) # cost function J

    return theta0, theta1, J
