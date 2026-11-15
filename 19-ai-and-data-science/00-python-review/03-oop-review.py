# class Color():
    
    
    
#     def black(self):
#         print("Black")
        
#     def red(self):
#         print("red")
        
# color = Color()
# color.black()
# color.red()

# color.blue = "blue"
# print(color.blue)

# color2 = Color()
# color2.black()
# print(color2.blue)

# class Circle():
    
#     def __init__(self, r):
    
#         self.r = r      # circle.raduis = 5
    
#     def diameter(self):
        
#         d = 2 * self.r
#         print(f"Diameter : {d}")
        
        
# circle = Circle(5)
# circle.diameter()
# print(circle.r)

# circle2 = Circle(3)
# circle2.diameter()
# print(circle2.r)


# Encabsulation


# Abstraction
# class Animal():
    
#     def move(self):
#         print("Walk")
    
#     def sound(self):
#         pass
    
# class Dog(Animal):
    
#     #Override
#     def move(self):
#         print("Run")
        
#     def sound(self):
#         print("Bark")
    


# # Inheratence
# class Snake(Animal):
    
#     #Override  -->  polymorphism "Run-Time polymorphism"
#     def move(self):
#         print("Crawl")
        
#     def sound(self):
#         print("Hiss")
    
        
        
        
# dog = Dog()
# snake = Snake()

# dog.move()
# snake.move()

# dog.sound()
# snake.sound()


# from AI_ML.name import *
# from AI_ML.age import *

# fname("Ola")
# print(f"Your Age Is {age(24)}")

# ---> Pypi


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
student = Student("Ahmed", 15)

print(f"Student Name Is : {student.name} , ANd His Age Is : {student.age}")