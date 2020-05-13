def fizz_buzz(leng):
    a = int (leng) 
    i = 0
    list = []
    while i < a:
        if (i % 15) == 0:
            list.append ("FizzBuzz")
        elif (i % 5) == 0:
            list.append ("Buzz")
        elif (i % 3) == 0:
            list.append ("Fizz")
        else:
            list.append (str (i))
        i += 1
    return print (list[:])

fizz_buzz (int (input ('Please enter number:')))



'''
fizz_buzz takes in an integer, length
It returns a list of strings that is 'length' strings long
For the each entry in the returned list: 
    - if the index is a multiple of three, the list element will be 'Fizz'
    - if the index is a multiple of five, the list element will be 'Buzz'
    - if the index is a multiple of both three and five, the list element will be 'FizzBuzz'
    - otherwise, the list element will be a string of the value of the index
'''
