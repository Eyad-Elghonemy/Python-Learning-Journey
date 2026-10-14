# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If It Has One Or More Abstract Methods
# - abc module in python provides Infrasstructure for Defining Custom AbstractBase Classes
# - By Adding @absttractmethod Decorator On The Methods
# - ABCMeta Class is A MetaClass Used For Defining Abstract Base Class
# ----------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Programming(metaclass = ABCMeta):   # Abstract Class
    
    @abstractmethod
    def has_oop(self):   # Abstract Method
        
        pass
    
    @abstractmethod
    def has_name(self):
        
        pass
    

class Python(Programming):
    
    def has_oop(self):
        
        return "Yes"
    
    
class Pascal(Programming):
    
    def has_oop(self):
        
        return "No"
    
    def has_name(self):
        
        pass
    
    

one = Pascal()

print(one.has_oop())


# print(one.has_name()
