#check if the length of the password is at least 8 characters

if __name__ == '__main__': 
        
    password = input()
    
    #write an if / else statement to evaluate passwords length
    if len(password) >= 8:
        print("Your password is long enough.")    
    else:
        print("Your password is too short.")