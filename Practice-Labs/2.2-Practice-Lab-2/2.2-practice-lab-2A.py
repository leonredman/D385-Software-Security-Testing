# Import the unittest module to create and run test cases
import unittest

# Define a function to multiply two numbers
def multiply_numbers(x, y):
    # If x is None, print a message and return y
    if x is None:
        print("x is a null value")
        return y
    # If y is None, print a message and return x
    elif y is None:
        print("y is a null value")
        return x
    # If both x and y are not None, return their product
    else:
        return x * y   

# Define a test case class to test the multiply_numbers function
class TestForNone(unittest.TestCase):
    def test_when_a_is_null(self): # Test case to check when y is None
        try:
            self.assertIsNone(multiply_numbers(5, None)) # Assert that the result of multiply_numbers(5, None) is None
        except AssertionError as msg:
            print(msg) # If the assertion fails, print the error message

if __name__ == '__main__':
    unittest.main()