# Import the Template class from the string module
from string import Template 

# Define a dictionary named CONFIG containing configuration data.
# In this case, it holds a single API_KEY with a string value.
CONFIG = {
    "API_KEY": "'you've just exposed your secret_key'"
}

# Define a class named User
class User:

    # Define class variables to store name and email attributes
    name = ""
    email = ""

    # Define the constructor (__init__) method to initialize the object with name and email
    def __init__(self, name, email):

        self.name = name
        self.email = email

    # Define the __str__ method to return the user's name when the object is converted to a string  
    def __str__(self):

        return self.name

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Get user input for name and email
    name = input()
    email = input()
    
    # Create a User object with the input data
    user = User(name, email)

    # Define a template string using the Template class
    name_template = Template("Hello, my name is $name.")

    # Use the `substitute()` method of the Template class to replace the variable in the template with the user's name
    greeting = name_template.substitute(name=name)

    # Print the greeting message
    print(greeting)