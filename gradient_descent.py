def gradient_descent(x, y, theta0, theta1, alpha, num_iters):
    m = len(y)  # number of training examples

    # Initialize theta0 and theta1 as lists with the initial values
    theta0 = [theta0]
    theta1 = [theta1]
    J = []  # cost function initialization

    for el in range(num_iters):
        h = [theta0[-1] + theta1[-1] * x_i for x_i in x]  # hypothesis
        # list theta0[-1] accesses the last element, theta0[-1] therefore equals theta0[el]
        error = [h_i - y_i for h_i, y_i in zip(h, y)]  # prediction error

        theta0.append(theta0[-1] - alpha / m * sum(error))
        theta1.append(theta1[-1] - alpha / m * sum(e_i * x_i for e_i, x_i in zip(error, x)))

        J.append(1 / (2 * m) * sum(e_i ** 2 for e_i in error))

    return theta0, theta1, J
