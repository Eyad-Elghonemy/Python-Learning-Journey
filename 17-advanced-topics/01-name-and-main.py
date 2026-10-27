# -----------------------------------------------
# -- Advanced Lessons => __name__ And __main__ --
# -----------------------------------------------
# if __name__   "__main__":

# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directory => Execute The Python File Using The command Line
# - From Import => Import The Code From To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ In The Background
# ---------------------------------------------------

print(__name__)

# File One

print("Print From File One")

    
if 1==1 :
        
    print("True")
        
else:
        
    print("Fale")
    

if __name__ == "__main__":
    
    print("File One Is Running Directly")
    
    def hello():
    
        print("Print Function From File One")
    
    
else :
    
    print("You Are NOT Running File One Directly")
    
hello() 



# File Two

import test

