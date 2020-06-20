import numpy as np


def times_table_numpy(np_number):
    b = int (np_number)
    primary_row = np.arange (0, b, 1)
    row = np.reshape (primary_row, (1, b))
    colum = np.reshape (primary_row, (b, 1))
    times_table_second = np.matmul (colum, row)
    new_aaray = times_table_second [(times_table_second % 7.5 == 0) & (times_table_second != 0)]
    number = len (new_aaray)
    print(new_aaray,number)
    return times_table_second

times_table_numpy(25)