"""
2.1 Practice Lab 1 Question

The purpose of this lab is to introduce students to the process of creating, accessing, and generating log files 
using code. Use the template provided in order to write code that outputs log information with the basic configuration
of level name and message, based on the information in the template.

When you divide a number by zero, write an error message to the log.

For Example, the following input:
0
9

The output to the console will be the following:

ERROR: The exception that occurred is: division by zero
Alternatively, if the input is:
10
2

The output to the console will be the following:
5.0

Alternatively, if the input is:
0
20

The output to the console will be the following:
0.0

Question - Supplied Code:
"""
import logging
import sys

import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

       quotient = dividend/divisor  
       print (quotient)
        
    except Exception as e:

        #logging error here, use str(e) as part of the output

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)