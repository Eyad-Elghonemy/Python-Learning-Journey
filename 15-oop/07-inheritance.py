# ------------------------------------------------
# -- Object Oriented Programming => inheritance --
# ------------------------------------------------


class Food :  # Base  # Parent 
    
    def __init__(self, name, price) -> None:
        
        self.name = name
        
        self.price = price
        
        print(f"{self.name} Is Created From Base Class And Price Is {self.price}")
        
    def eat(self):
        
        print("Eat Method From Base Class")
        

class Apple(Food) :  # Derived Class  # Child
    
    def __init__(self, name, price, amount) -> None :
        
        # Food.__init__(self,name)   # Create Instance From Base Class
        
        super().__init__(name, price)
        
        self.amount = amount
        
        # self.name = name
        
        # self.price = price + 20  # OverWrite
         
        print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")
        
    
    def get_from_tree(self):
        
        print("Get From Tree From Derived Class")
        
        
 
# food_one = Food("Pizza", 150)

food_two = Apple("Pizza", 150, 500)

food_two.eat()

food_two.get_from_tree()

