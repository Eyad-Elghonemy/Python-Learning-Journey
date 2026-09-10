# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Eelement
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolen Value
# ----------------------------------------------------------------
 
# Example 1

def checknum(num):
    
    return num > 10 

mynums = [1, 19, 10, 20, 100, 5, 0, 0, 0]

myresult = filter(checknum, mynums)

for number in myresult :
    
    print(number)

print('#'*50)

# Example 2

def checkname(name):
    
    return str(name).startswith("O") 

mytexts = ["Osama", "Omer", "Omar", "Ahmed", "Osman", "Sayed"]

myreturneddata = filter(checkname, mytexts)

for person in myreturneddata :
    
    print(person)
    
print('#'*50)

# Example 3

# def checkname(name):
    
#     return str(name).startswith("O") 

mynames = ["Osama", "Omer", "Omar", "Ahmed", "Osman", "Sayed", "Amer"] 

for p in filter(lambda name : str(name).startswith("A"), mynames) :
    
    print(p)
    
 