import numpy as np

def normalize_minmax_list(list):
    min_el = min(list)
    max_el = max(list)
    list_normalized = [(x_i - min_el)/(max_el - min_el) for x_i in list]
    return list_normalized, min_el, max_el

def normalize_zscore_list(list):
    list_mean = np.mean(list, axis=0)
    list_std = np.std(list, axis=0)
    print("mean : {} - std : {}".format(list_mean, list_std))
    list_normalized = (list - list_mean) / list_std
    return list_normalized, list_mean, list_std