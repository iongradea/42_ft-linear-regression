import csv

def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        x_km = []
        y_price = []
        for row in csvreader:
            x_km.append(row[0])
            y_price.append(row[1])
            # print(', '.join(row))
        x_km.pop(0)
        y_price.pop(0)
    return(x_km, y_price)

def convert_list_to_float(list):
    for el in range(len(list)):
        list[el] = float(list[el])
    return list