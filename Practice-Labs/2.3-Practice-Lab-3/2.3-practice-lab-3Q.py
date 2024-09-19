"""
An attacker was able to get access to sensitive information. Fix the 
templated code provided below to make it more secure.

Sample Input:

Jane Doe
jane_doe@email.com
If the code is not fixed properly, the output to the console will be:

The secret is 'you've just exposed your secret_key'
Alternatively, when the code is fixed properly the output to the console 
should be:

Hello, my name is Jane Doe.
Hint: Python objects can access internal attributes, including a 
dictionary of global variables. You can eliminate such vulnerabilities 
by avoiding invalidated user inputs. Create a string template object to 
create simplified syntax for output specification and then map that 
object with the keyword argument. Be sure to use the Template class 
which is a safer method to create a simple template string.
"""

from string import Template

CONFIG = {

    "API_KEY": "'you've just exposed your secret_key'"
}
class User:

    name = ""
    email = ""

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def __str__(self):

        return self.name
        
if __name__ == '__main__':
    name = input()
    email = input()
    
    user = User(name, email)
    
    # FIXME:  Here is where you want to use the template class
    print(f"The secret is {user.__init__.__globals__['CONFIG']['API_KEY']}")
  