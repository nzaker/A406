import unittest
import fizzbuzz

'''
YOU MAY NOT EDIT THIS FILE! UNDER PAIN OF BEING TOLD TO GO BACK AND DO THE ASSIGNMENT AGAIN, BUT PROPERLY!
You may, however, admire the unittests, you will grow to love them soon.
'''

class fizz_buzz_test(unittest.TestCase):
    '''
    Test cases for the fizz_buzz function
    '''
    def test_length_20(self):
        expected_result = [
            'FizzBuzz', 
            '1', 
            '2', 
            'Fizz', 
            '4', 
            'Buzz', 
            'Fizz', 
            '7', 
            '8', 
            'Fizz', 
            'Buzz', 
            '11', 
            'Fizz', 
            '13', 
            '14', 
            'FizzBuzz', 
            '16', 
            '17', 
            'Fizz', 
            '19',
            ]
        
        self.assertEqual(fizzbuzz.fizz_buzz(20), expected_result)
    
    def test_length_7(self):
        expected_result = [
            'FizzBuzz', 
            '1', 
            '2', 
            'Fizz', 
            '4', 
            'Buzz', 
            'Fizz', 
            ]
    
        self.assertEqual(fizzbuzz.fizz_buzz(7), expected_result)
    
    def test_length_0(self):
        self.assertEqual(fizzbuzz.fizz_buzz(0), [])

if __name__ == '__main__':
    unittest.main()
