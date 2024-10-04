#Simulated auhorization code

ownerID = 4567

def ShowData():
    if(GetUserID() == ownerID):
        print("This is the user data")
def Redirect():
    print("Redirecting to homepage")
def GetUserID():
    return 1234

if(not GetUserID() == ownerID):  # this is just a simulation, this line is typically !$_GET['userID'] === object.ownerID
    print( "You are not allowed to view this data")
    Redirect()

ShowData()