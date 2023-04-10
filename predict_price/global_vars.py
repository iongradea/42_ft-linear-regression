import argparse

res_file = "./model_res/res.json"

def program_mode():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Getting command line options")

    # Add command-line options
    parser.add_argument("-v", "--verbose", type=int, choices=[0, 1], default=1, help="Enter the verbosity level : 0 (no print), 1 (basc info)")

    # Parse the command-line options
    args = parser.parse_args()

    print("[verbosity 0] verbosity = {}".format(args.verbose)) if args.verbose >= 0 else None
    return args.verbose


verbosity = program_mode()