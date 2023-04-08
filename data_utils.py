import csv

def program_mode():
    try:
        print_level = int(input('[program_mode - print level] What print policy level do you want between : 0 (no print), 1 (basic info), 2 (debug) ? By default it is 1 ... '))
        if print_level in [0, 1, 2]:
            print("[program_mode - print level] Print policy level chosen : {}".format(print_level))
        else:
            print("[program_mode - print level] Default chosen : 1")
            print_level = 1
    except Exception as e:
        print("[program_mode - print level] Default chosen : 1")
        print_level = 1
    try:        
        normalization = input('[program_mode - normalization] What normalization method do you want (z for z-score, m for minmax) ? Default is z-score ... ')
        if normalization == 'm':
            print("[program_mode - normalization] minmax normalization chosen!")
        elif normalization == 'z':
            print("[program_mode - normalization] z-score normalization chosen!")
        else:
            print("[program_mode - normalization] Default chosen : z-score!")
            normalization == 'z'
    except Exception as e:
        print("[program_mode - normalization] Default chosen : z-score!")
        normalization == 'z'
    try:
        alpha = float(input("[program_mode - parameters] Please enter the alpha value (default is 0.01) : "))
        num_iters = int(input("[program_mode - parameters] Please enter the number of iterations (default is 10000) : "))
    except Exception as e:
        print("[program_mode - parameters] Default chosen : alpha = 0.01, num_iters = 10000")
        alpha = 0.01
        num_iters = 10000
    return print_level, normalization, alpha, num_iters

def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        x_km = []
        y_price = []
        for row in csvreader:
            x_km.append(row[0])
            y_price.append(row[1])
        x_km.pop(0)
        y_price.pop(0)
    return(x_km, y_price)

def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list