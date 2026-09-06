# def reverse_string(my_string):
    
#     for x in my_string[::-1] :
    
#         yield x
    

# for c in reverse_string("Elzero"):
#     print(c)

def sugar(func) :
    
    def wrapper() :
        
        print("Sugar Added From Decorators")
        
        func()
        
        print('#')
        
    return wrapper

@sugar

def make_tea():
  print("Tea Created")

@sugar

def make_coffe():
  print("Coffe Created")
  
make_tea()
make_coffe()
