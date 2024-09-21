
# Define a function to convert temperature from Celsius to Fahrenheit
def CelciusToFahrenheit(Temperature):

    # Insert an assert statement to check if the temperature is greater than 0
    # If the temperature is not greater than 0, an AssertionError will be raised
    #  with the specified message
    assert Temperature >= 0, "Colder than zero degrees Celsius!"

    
    # Convert the int of Celsius to Fahrenheit and return the result
    return ((Temperature*9)/5)+32

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    
    # Get user input for the temperature in Celsius
    Temperature = int(input())

    try:
        # Call the CelciusToFahrenheit function with the user-provided 
        # temperature
        # If the temperature is colder than zero, an AssertionError will 
        # be raised and caught in the except block
        print(CelciusToFahrenheit(Temperature))

    # If an AssertionError occurs, print the error message specified in the 
    # assert statement
    except AssertionError as msg:
        print(msg)