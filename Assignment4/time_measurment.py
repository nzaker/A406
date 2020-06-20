import numpy as np
import timeit

time_1= timeit.timeit('''def times_table_lists(number):
 a=int(number)
 times_table = [[]*a] * a
 pattern = list(range(0, a))
 for i in range ( 0, a):
     times_table[i] =[ m * i for m in pattern ]
 return  times_table''', number=1500)

time_2= timeit.timeit('''def times_table_numpy(np_number):
   b = int (np_number)
   primary_row = np.arange(0,b,1)
   row = np.reshape(primary_row, (1,b))
   colum = np.reshape(primary_row, (b,1))
   times_table_second = np.matmul(colum,row)
   return times_table_second''', number=1500)
print('time for list is :', time_1)
print('time for numpy is :', time_2)