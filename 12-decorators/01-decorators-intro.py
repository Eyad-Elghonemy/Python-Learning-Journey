# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometime Called Meta Programming
# [2] Everything In Python Is Object Even Functions
# [3] Decorator Take A Function And Add Some Fuctionality And Return It
# [4] Decorator Wrap Other Function And Enhance Thier Behavior
# [5] Decorator Is Higher Order Function (Function Accept Function As A Parameter)
# --------------------------------------------------------------------------

def mydecorate(func) : # Decorator
    
    def neastedfunc() : # Any Name Its just For Decoration
        
        print("Before")  # Message From Decorator
         
        func()  # Excute Function
        
        print("After")  # Message From Decorator
        
    return neastedfunc  # Return All Data

@mydecorate

def sayhello() :
    
    print("Hello From Hello Function")
    


def sayhowareyou() :
    
    print("Hello From Hello Function How Are You")
    
# afterdecoration = mydecorate(sayhello)

# afterdecoration()

sayhello()

print('$'*50)    

sayhowareyou()