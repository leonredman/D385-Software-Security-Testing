"""
For this lab you will use unit testing to check a null setting using assertions. 
Use the commented template code provided to do the following:

Use the assertIsNone() function from Python’s unittest library to verify whether an input 
value is “None” or “not” using a test case. A Boolean value should be returned by this 
function based upon the assert condition that the two parameter inputs are received. .

The assertIsNone() function will return true if the input value is equal to "None", and false 
if it is not. In the multiply_numbers function, test for all cases of a null value. 
Return the not-null value for each condition with a print statement of the null value.

For example, the output to the console from the source code multiply_numbers(5, None) 
will be the following output:

y is a null value
5 is not None
"""

# unit test case
import unittest

def multiply_numbers(x, y):  
    #add your code here
    return x * y
    #add your code here

class TestForNone(unittest.TestCase):
        
    def test_when_a_is_null(self):
        try:
            self.assertIsNone(multiply_numbers(5, None))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':  
    unittest.main()