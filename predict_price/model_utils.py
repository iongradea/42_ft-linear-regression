def create_function(theta, y_norm_vars, normalization, normalize_y, plot_normalize_y):
    # assign values
    [theta0, theta1] = theta 
    [min_y, max_y, std_y, mean_y] = y_norm_vars

    # unormalize y if necessary
    if normalize_y == 'y':
        if plot_normalize_y == 'y':
            predict_price = lambda x: theta0 + theta1 * x
        else:
            if normalization == 'm':
                predict_price = lambda x: (theta0 + theta1 * x) * (max_y - min_y) + min_y
            else:
                predict_price = lambda x: (theta0 + theta1 * x) * std_y + mean_y
    else:
        predict_price = lambda x: theta0 + theta1 * x
    return predict_price