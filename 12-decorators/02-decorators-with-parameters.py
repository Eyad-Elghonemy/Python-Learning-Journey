# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------


def mydecorate(func) : # Decorator
    
    def neastedfunc(num1, num2) : # Any Name Its just For Decoration
        
        if num1 < 0 or num2 < 0 :
            
            print("Be Ware One Of The Numbers or Two Numbers Is Less Than Zero")
         
        func(num1, num2)  # Excute Function
        
        
    return neastedfunc  # Return All Data


def mydecorator2(func) : # Decorator
    
    def neastedfunc(num1, num2) : # Any Name Its just For Decoration
        
        print("Coming From Decorator Two")
         
        func(num1, num2)  # Excute Function
        
        
    return neastedfunc  # Return All Data

@mydecorate
@mydecorator2
def  calculate(n1, n2) :
    
    print(n1 + n2)
    
    
calculate(-5,90)