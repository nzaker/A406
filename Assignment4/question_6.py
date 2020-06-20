import numpy as np


def times_table_numpy(np_number):
    b = int (np_number)
    primary_row = np.arange (0, b, 1)
    row = np.reshape (primary_row, (1, b))
    colum = np.reshape (primary_row, (b, 1))
    times_table_second = np.matmul (colum, row)
    number_of_divisable = 0
    new_array = np.array ([])

    for i in times_table_second:
        for j in i:
            if j % 7.5 == 0 and j != 0:
                new_array = np.append (new_array, j)
                number_of_divisable += 1

    print (number_of_divisable, new_array)
    return times_table_second


times_table_numpy (25)
