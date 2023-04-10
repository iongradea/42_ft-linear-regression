import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x_km, y_price, y_res, y_fn):
    # initiliaze the figure
    fig1, ax1 = plt.subplots()
    ax1.set_xlabel('x km')
    ax1.set_ylabel('y price')
    ax1.set_title('price by km')
    
    # plotting the points
    ax1.scatter(x_km, y_price, marker="x", label="y_price")
    ax1.scatter(x_km, y_res, marker="o", label='y_res')

    # Generate x values
    # x = list(range(0, 250000, 1000))
    x_values = np.linspace(10000, 250000, 1000)
    # Calculate y values using the lambda function
    # y_values = [y_fn(x) for x in x_values]
    y_values = y_fn(x_values)
    # Plot the function
    ax1.plot(x_values, y_values, color='green', label='y_fn')
    ax1.legend()


def plot_cost(J):
    fig2, ax2 = plt.subplots()
    ax2.set_xlabel('Number of iterations')
    ax2.set_ylabel('Cost function')
    ax2.set_title('Cost function')
    iterations = list(range(len(J)))
    ax2.plot(iterations, J, label='Cost function J')
    ax2.legend()


def plot_graphs(x_km, y_price, y_res, J, y_fn):
    # Enable interactive mode
    plt.ion()

    # Plot the data
    plot_graph(x_km, y_price, y_res, y_fn)

    # Plot the cost function
    plot_cost(J)

    # Disable interactive mode
    plt.ioff()

    # Keep the plot open until the user closes it
    plt.show(block=True)