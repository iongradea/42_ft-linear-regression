import matplotlib.pyplot as plt

def plot_graph(x_km, y_price, y):
    plt.xlabel('X km')
    plt.ylabel('Y price')
    plt.title('XY km/price')
    plt.scatter(x_km, y_price, marker="x")
    plt.scatter(x_km, y, marker="o")
    plt.show()

def plot_cost_function(J):
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost function')
    plt.title('Cost function')
    iterations = list(range(len(J)))
    plt.plot(iterations, J)
    plt.show()