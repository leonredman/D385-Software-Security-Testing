"""
Assertions can be an excellent tool if you're looking for a way to 
increase the effectiveness of your debugging and testing processes. 
In the following lab, you will demonstrate the basics of using assert 
statements, including how to write logical statements and when to 
use assertion statements in your code.

Using the templated code provided, write an assertion statement where 
noted in the template code. The assertion statement needs to determine 
whether an integer input is below freezing using the phrase: 
"Colder than zero degrees Celsius!".

For example if the input is
-5

The output to the console for your assertion statement will be the 
following:
Colder than zero degrees Celsius!

If the input is greater than zero degrees Celsius 
(note: this code is already provided):
5

The output to the console in Fahrenheit will be the following:
41
"""

def CelciusToFahrenheit(Temperature):
    #insert assert statement for, "Colder than zero degrees Celsius!"
 
    return ((Temperature*9)/5)+32

if __name__ == '__main__':  
    Temperature = int(input())
    try:
        print(CelciusToFahrenheit(Temperature))
    except AssertionError as msg:
        print(msg)