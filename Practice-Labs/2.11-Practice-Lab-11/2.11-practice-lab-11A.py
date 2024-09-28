#check if the input range is between 1 and 10 for the range validation check

if __name__ == '__main__': 
        
    r = range(1,10)
    
    num = int(input())
    
    # create conditional statement for range check here
    if num in r:
        print("The number input is in the range from 1 and 10.")
    else:
        print("The number input is not in the range from 1 and 10.")