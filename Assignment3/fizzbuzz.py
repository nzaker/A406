def fizz_buzz(length):
    if (length % 15) == 0:
        return print("FizzBuzz")
    elif (length % 5) == 0:
        return print("Buzz")
    elif (length % 3) == 0:
        return print("Fizz")
    else:
        return print (chr(length))



fizz_buzz(len(input("please enter a name: ")))

'''
fizz_buzz takes in an integer, length
It returns a list of strings that is 'length' strings long
For the each entry in the returned list: 
    - if the index is a multiple of three, the list element will be 'Fizz'
    - if the index is a multiple of five, the list element will be 'Buzz'
    - if the index is a multiple of both three and five, the list element will be 'FizzBuzz'
    - otherwise, the list element will be a string of the value of the index
'''
