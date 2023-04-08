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

        tmptheta0 = alpha / m * sum(error)  # step for theta0 : alpha * dJ / dtheta0
        tmptheta1 = alpha / m * sum(e_i * x_i for e_i, x_i in zip(error, x))  # step for theta0 : alpha * dJ / dtheta1

        theta0.append(theta0[-1] - tmptheta0) # gradient descent for theta0
        theta1.append(theta1[-1] - tmptheta1) # gradient descent for theta1

        J.append(1 / (2 * m) * sum(e_i ** 2 for e_i in error)) # cost function J

    return theta0, theta1, J
