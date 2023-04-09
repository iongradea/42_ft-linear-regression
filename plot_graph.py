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

# def plot_():
#     # Enable interactive mode
#     plt.ion()

#     # Generate some data for the plots

#     # Create a single figure and axes
#     fig, ax = plt.subplots()
#     ax.set_title("Sine and Cosine Functions")

#     # Update the graph in a loop (in this example, the loop runs 5 times)
#     for _ in range(5):
#         # Clear previous data
#         ax.clear()

#         # Update data for the plots
#         y1 = np.sin(x)
#         y2 = np.cos(x)

#         # Plot the updated data as points
#         ax.plot(x, y1, 'o', label='sin(x)')  # 'o' specifies the point marker style
#         ax.plot(x, y2, label='cos(x)')  # 'o' specifies the point marker style

#         # Add titles and labels
#         ax.set_title("Sine and Cosine Functions")
#         ax.set_xlabel("x")
#         ax.set_ylabel("y")
#         ax.legend()

#         # Pause for a short period to allow the graph to update
#         plt.pause(0.1)

#         # Shift the x values for the next iteration
#         x += 0.1

#     # Disable interactive mode
#     plt.ioff()

#     # Keep the plot open until the user closes it
#     plt.show(block=True)