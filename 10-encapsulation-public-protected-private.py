# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation  # نظام التغليف
# - Restrict Access To the Data Stored In Atrributes And Methods 
# Public
# - Every Attribute And Method That We Used So Far Is Public
# - Attributes And Methods Can Be Modifed And Run From Everywhere 
# - Inside Our Outside The Class 
# Protected
# - Attributes And Methods Can Be Accessed From Within The Class And Sub Classes (Inherted Classes)
# - Attributes And Methods Prefixed With One Underscore _
# Private
# - Attributes And Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From outside The Class
# - Attributes And Methods Prefixed With Two Underscore __
# --------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

# Public

# class Member:
    
#     def __init__(self, name) :
        
#         self.name = name  # Public
        
# one = Member("Ali")

# print(one.name)

# one.name = "Sayed"

# print(one.name)

##################################################### # protected

# class Member:
    
#     def __init__(self, name) :
        
#         self._name = name  # Public
        
# one = Member("Ali")
# print(one._name)

# one._name = "Sayed"

# print(one._name)

##################################################### # Private

class Member:
    
    def __init__(self, name) :
        
        self.__name = name  # Public

    def say_hello(self):
        
        return f"Hello {self.__name}"
        
one = Member("Ali")
# print(one.__name) # Error
print(one.say_hello())

print(one._Member__name)