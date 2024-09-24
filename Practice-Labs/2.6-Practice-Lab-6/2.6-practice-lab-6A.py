
def check_numeric_value(wg_int):
    return isinstance(wg_int, int)
    
        #return true if numeric value is an integer, else return false.  
        #Hint: use isinstance function

# verify if the string is null

def check_null_string (wg_string):
    
    # check if wg_string is not null return true else return false
    return wg_string is not None
       
if __name__ == '__main__':  
    
    wg_string = "I like dogs." # use keyword None to test
    wg_int = 12345
    
    print(check_null_string (wg_string))
    print(check_numeric_value(wg_int))