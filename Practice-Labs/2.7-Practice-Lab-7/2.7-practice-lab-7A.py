import hashlib

def hash_password(pwd):
    # encode password string to bytes
    enc_pwd = pwd.encode()
    
    # call the sha3_256() function returns a hash object
		# call update on the encoded password string
    d = hashlib.sha3_256()
    d.update(enc_pwd)
    
    # generate binary hash of password string in hexidecimal
    hash = d.hexdigest()
    
    return hash
    
if __name__ == '__main__':
    pwd = "Password"
    
    print(hash_password(pwd))