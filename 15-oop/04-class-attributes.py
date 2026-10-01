# ------------------------------------------------------
# -- Object Oriented Prograamming => Class Attributes --
# ------------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructctor
# -------------------------------------------------------------


class Member :
        
    not_allowed_names = ["Hell", "Shit", "Baloot"]  # Out Of The Constructor
    
    member_num = 0
    
    
    def __init__(self, first_name, middle_name, last_name, gender):
        
        
        
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        
        Member.member_num += 1 
        
        
    def full_name(self):
        
        if self.fname in Member.not_allowed_names :
            
            raise ValueError ("Name Not Allowed")
        
        return f"{self.fname} {self.mname} {self.lname}"
    
    def name_with_title(self):
        
        if self.gender == "Male" :
            
            return f"Hello Mr {self.fname}"
        
        elif self.gender == "Female" :
            
            return f"Hello Ms {self.fname}"
        
        else :
            
            return f"Hello {self.fname}"
        
    
    def get_all_info(self) :
        
        return f"{self.name_with_title()}, Your Full Name Is : {self.full_name()}"

    
    def delete_users(self):
        
        Member.member_num -= 1
        
        return f"User {self.fname} Deleted"

    
print(Member.member_num)

member_one = Member("Osama", "Mohamed", "Alsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.member_num)

print(member_four.delete_users())

print(Member.member_num)
 
# print(member_three.get_all_info())
# print(member_four.get_all_info())