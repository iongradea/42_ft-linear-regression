import argparse

def program_mode():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Getting command line options")

    # Add command-line options
    parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], default=1, help="Enter the verbosity level : 0 (no print), 1 (basc info), 2 (debug)")
    parser.add_argument("-n", "--normalization", type=str, choices=["m", "z"], default="z", help="Enter the normalization method : m for minmax, z for z-score")
    parser.add_argument("-ny", "--normalize_y", type=str, choices=["y", "n"], default="n", help="Normalize y values (prices) : y for yes, n for no")
    parser.add_argument("-pny", "--plot_normalize_y", type=str, choices=["y", "n"], default="n", help="Plot normalize y values (prices) : y for yes, n for no")
    parser.add_argument("-a", "--alpha", type=float, default=0.01, help="Enter the alpha value")
    parser.add_argument("-i", "--num_iters", type=int, default=1000, help="Enter the number of iterations")

    # Parse the command-line options
    args = parser.parse_args()

    return args.verbose, args.normalization, args.normalize_y, args.plot_normalize_y, args.alpha, args.num_iters


verbosity, normalization, normalize_y, plot_normalize_y, alpha, num_iters = program_mode()
