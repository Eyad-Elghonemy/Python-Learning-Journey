# -----------------------------------------
# -- Decoorators => Practical Speed Test --
# -----------------------------------------

from time import time

# def mydecorate(func) : # Decorator
    
#     def neastedfunc(*nums) : # Any Name Its just For Decoration
        
#         for num in nums :
            
#             if num < 0 :
            
#                 print("Be Ware One Of The Numbers or Two Numbers Is Less Than Zero")
        
         
#         func(*nums)  # Excute Function
        
        
#     return neastedfunc 

# @mydecorate

# def calculate(n1, n2, n3, n4) :
    
#     print(n1 + n2 + n3 + n4)
    
# calculate(-5, 90, 50, 150)
    
    
def speedtest(func) :
    
    def wrapper() :
        
        start = time()
        
        func()
        
        end = time()
        
        print(f"Function Running Time IS {end - start}")
        
    return wrapper

@speedtest

def bigloop() :
    
    for num in range(1, 20000) :
        
        print(num)

bigloop()