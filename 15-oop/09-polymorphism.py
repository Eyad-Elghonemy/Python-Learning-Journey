# -------------------------------------------------
# -- Object Oriented Programming => polymorphism --
# -------------------------------------------------

n1 = 10
n2 = 20 

print(n1 + n2)  # Addition

print("#"*50)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)  # Concatunation

print("#"*50)

print(len([1,2,3,4,5,6]))
print(len("OSama Elzero"))
print(len({"key_one" : 2, "key_two" : 3}))

print("#"*50)

class A :
    
    def do_something(self):
        
        print("From Class A")
        
        raise NotImplemented ("Derived Class Not Implement This Method")
        

class B(A):
    
    def do_something(self):
        
        print("From Class B")
        

class C(A):
    
    def do_something(self):
        
        print("From Class C")
   



my_instance = C()

my_instance.do_something()