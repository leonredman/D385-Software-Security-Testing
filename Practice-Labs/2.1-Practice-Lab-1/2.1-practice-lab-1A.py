import logging
import sys

# Define a function to handle division by zero error and log it while printing the output to the screen.
def divideByZeroError(dividend, divisor):

    # Configure the logging module to output messages to sys.stdout with a specific format.
    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:
	    # Attempt division to get the quotient.
	    quotient = dividend/divisor
	    print (quotient)
        
    except Exception as e:

	    # If an exception occurs during division, log the error using the logging module, including the exception message (str(e)).
	    logging.error(' The exception that occured is: ' + str(e))

if __name__ == '__main__': 
	# Get the values for dividend and divisor from user input.
	dividend = int(input())
	divisor = int(input())
	
	# Call the divideByZeroError function with the provided input values to handle any potential division errors.
	divideByZeroError(dividend,divisor)