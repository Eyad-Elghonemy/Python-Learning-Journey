# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything In Python Is An Object
# __init__ Called Automatically When Installing Class
# self.__class__ The Class TO Which A Class Instance Belongs
# __str__  Gives A Human Readable Output Of The Object
# __len__  Returns The Length Of The Container
#          Called When We Use The Built-In len() Function On The Object
# -----------------------------------------------------

class Skill :
    
    def __init__(self):
        
        self.skills = ["HTML", "CSS", "JS"]

    def __str__(self):
        
        return f"This Is My Skills => {self.skills}"
    
    def __len__(self):
        
        return len(self.skills)

profile = Skill()

print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MYSQL")

print(len(profile))

# print(profile.__class__)  # Belong To Class Skill

# my_string = "Osama"
# print(type(my_string))
# print(my_string.__class__)

# print(dir(str))

# print(str.upper(my_string))

###############################################################################
# print(instanceName.methodName()) == Print(className.methodName(instanceName))
###############################################################################

