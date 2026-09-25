import re

file = open(r"C:\Users\eyad0\Accounts.txt", "r")

email = None

password = None



v = file.read().count("Email")

f = int(file.readlines(-1).count("Password"))



def total_and_close():

    """
    This Function Used To Count Total Accounts In System And Close File
    """

    v = file.read().count("Email")

    print(f"You Have {v} Accounts In System")
    
    file.close()

    print("File Closed")


while email == None :
    

    email_user = input("Enter The Valid Email :")

    if re.search(r"([A-z0-9]{6,})@([A-z]+)(\.com)", email_user):
            
        file = open(r"C:\Users\eyad0\Accounts.txt", "a")

        email = email_user
        
        file.write(f"{v+1}-Email => " + email + " ==> ")
        



    else :

        print("Invalid Email Please Try Again")


while password == None :
    
    password_user = input("Enter The Valid Password :")

    if re.search(r"([A-Z]+)([a-z]+)(\d+)",password_user):

        password = password_user

        file.write("Password => " + password +"\n")

        file = open(r"C:\Users\eyad0\Accounts.txt", "r")
        

    else :

        print("Invalid Password Please Try Again")

else :

    total_and_close()

