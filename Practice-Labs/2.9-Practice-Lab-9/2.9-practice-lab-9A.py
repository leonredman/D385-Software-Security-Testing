# check if the zipcode input is numeric

if __name__ == '__main__': 
        
    zipCode = input()
    
    try:
        #check that zip code is an integer value
        
        zip_check = int(zipCode)
        print(f'Your zip code is {zipCheck}.')

    except ValueError:
        print('Please use numeric digits for the zip code.')
