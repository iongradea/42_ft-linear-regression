#!/usr/local/bin/python3

# function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)


def gradient_descent(x, y, theta0, theta1, alpha, num_iters):
    m = len(y)  # number of training examples
    h = theta0 + theta1 * x  # hypothesis

    # h0 = theta0 + theta1 * x[0]  # Hypothesis for x0
    # h1 = theta0 + theta1 * x[1]  # Hypothesis for x1
    # h2 = theta0 + theta1 * x[2]  # Hypothesis for x2

    error = h - y  # prediction error

    # J = 1 / (2 * m) * sum(error ** 2)  # cost function
    # sum(error ** 2) = (h0 - y0) ** 2 + (h1 - y1) ** 2 + (h2 - y2) ** 2 ...

    # error0 = h0 - y[0]  # Prediction error for x0
    # error1 = h1 - y[1]  # Prediction error for x1
    # error2 = h2 - y[2]  # Prediction error for x2

    theta0 = [0] # theta0 initialization
    theta1 = [0] # theta1 initialization
    J = [] # cost function initialization

    for el in range(0,num_iters - 1):
        theta0[el+1] = theta0[el] - alpha / m * sum(error) 
        theta1[el+1] = theta1[el] - alpha / m * sum(error * x)
        J[el+1] = 1 / (2 * m) * sum(error ** 2) # cost function 
        # sum(error ** 2) = (h0 - y0) ** 2 + (h1 - y1) ** 2 + (h2 - y2) ** 2 ...

    return theta0, theta1, J


def gradient_descent(x, y, theta0, theta1, alpha, num_iters):
    m = len(y)  # number of training examples
    h = theta0 + theta1 * x  # hypothesis

    error = h - y  # prediction error

    theta0 = [0] # theta0 initialization
    theta1 = [0] # theta1 initialization
    J = [] # cost function initialization

    for el in range(0,num_iters - 1):
        theta0[el+1] = theta0[el] - alpha / m * sum(error) 
        theta1[el+1] = theta1[el] - alpha / m * sum(error * x)
        J[el+1] = 1 / (2 * m) * sum(error ** 2) # cost function 
        # sum(error ** 2) = (h0 - y0) ** 2 + (h1 - y1) ** 2 + (h2 - y2) ** 2 ...

    return theta0, theta1, J


# Data points
x = [x0, x1, x2]
y = [y0, y1, y2]

# Initialize parameters
theta0 = 0
theta1 = 0

# Gradient descent settings
alpha = 0.01
m = 3

# Perform one gradient descent step
h0 = theta0 + theta1 * x[0]  # Hypothesis for x0
h1 = theta0 + theta1 * x[1]  # Hypothesis for x1
h2 = theta0 + theta1 * x[2]  # Hypothesis for x2

error0 = h0 - y[0]  # Prediction error for x0
error1 = h1 - y[1]  # Prediction error for x1
error2 = h2 - y[2]  # Prediction error for x2

theta0 = theta0 - alpha / m * (error0 + error1 + error2)
theta1 = theta1 - alpha / m * (error0 * x[0] + error1 * x[1] + error2 * x[2])
