import unittest
import timestable
import numpy as np

'''
YOU MAY NOT EDIT THIS FILE! UNDER PAIN OF BEING TOLD TO GO BACK AND DO THE ASSIGNMENT AGAIN, BUT PROPERLY!
You may, however, admire the unittests, you will grow to love them soon (or not!)
'''

class times_table_lists_test(unittest.TestCase):
    '''
    Test cases for the times_table_lists
    '''
    def test_selected_values(self):
        '''
        Some selected indices are correctly calculated;
        the size of the list of lists is correct; and 
        the output is a list.
        '''
        expected_result = [24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76]
        expected_size = 20
        
        actual_result = timestable.times_table_lists(20)
        
        self.assertEqual(actual_result[4][6:], expected_result)
        self.assertEqual(len(actual_result), expected_size)
        self.assertEqual(len(actual_result[0]), expected_size)
        self.assertTrue(isinstance(actual_result, list))
    
class times_table_numpy_test(unittest.TestCase):
    '''
    Test cases for the times_table_numpy
    '''
    def test_selected_values(self):
        '''
        Some selected indices are correctly calculated;
        the size of the numpy array is correct; and
        the output is a numpy array.
        '''
        expected_result = np.array(
            [
                [24, 32], 
                [36, 48], 
                [48, 64]
            ])
        expected_size = (20, 20)
        
        actual_result = timestable.times_table_numpy(20)
        
        np.testing.assert_array_equal(actual_result[4:10:2, 6:10:2], expected_result)
        self.assertEqual(np.shape(actual_result), expected_size)
        self.assertTrue(isinstance(actual_result, np.ndarray))
    
if __name__ == '__main__':
    unittest.main()
