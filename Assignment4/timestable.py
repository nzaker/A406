import numpy as np
from numpy.core._multiarray_umath import ndarray


def times_table_lists(number):
 a=int(number)
 times_table = [[]*a] * a
 pattern = list(range(0, a))
 for i in range ( 0, a):
     times_table[i] =[ m * i for m in pattern ]
 return  times_table

'''
k=input('Please enter the Times Table\'s size: ')
'''
times_table_lists(7)



def times_table_numpy(np_number):
   b = int (np_number)
   primary_row = np.arange(0,b,1)
   row = np.reshape(primary_row, (1,b))
   colum = np.reshape(primary_row, (b,1))
   times_table_second = np.matmul(colum,row)
   return times_table_second

'''
l=input('Please enter the Times Table\'s size for calculating by numpy: ')
'''
times_table_numpy(25)
