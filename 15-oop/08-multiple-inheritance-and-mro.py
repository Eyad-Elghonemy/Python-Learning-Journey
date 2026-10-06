# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple inheritance --
# ---------------------------------------------------------

        
# food_one = Food("Pizza", 150)

# food_two = Apple("Pizza", 150, 500)

# food_two.eat()          # Over Ride

# food_one.eat()

class BaseOne:
    
    def __init__(self):
        
        print("Base One")


    def func_one(self):
        
        print("One")
    
    
class BaseTwo:
    
    def __init__(self):
        
        print("Base Two")
        
    def func_two(self):
        
        print("Two")


class Derived(BaseOne, BaseTwo):
    
    pass

my_var = Derived()

print(Derived.mro())  # method resolution oreder

print(my_var.func_one)
print(my_var.func_two)

print('#'*50)

my_var.func_one()
my_var.func_two()


print('#'*50)


class Base:
    
    def __init__(self):
        
        pass
    
    def shit(self):
        
        print("Shit base")
        

class DerivedOne(Base):
    
    pass

class DerivedTwo(DerivedOne):
    
    pass


shit_one = Base()

shit_two = DerivedOne()

shit_three = DerivedTwo()


shit_one.shit()
shit_two.shit()
shit_three.shit()