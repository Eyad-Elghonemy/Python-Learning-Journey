# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax And Info --
# ----------------------------------------------------------
# [01] Class Is The BluePrint Or Construtor Of The Object  # مخطط
# [02] Class Instantiate Means Create Instance Of A Class
# [03] Instance => Object Created From Class And Have thier Methods And Attributes
# [04] Class Defined With Keyword calss
# [05] Class Name Written With pascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods And Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Intialize The Data For The Object
# [10] Any Method With Two Underscore In The Start And End Called Dunder Or Magic Method
# [11] Self Refer To Current Instance Created From The class And Must Be First Param
# [12] Self Can Be Named Anything
# [13] In Python You Don't Neef To Call new() Keyword To Create Object
# --------------------------------------------------------------------


# syntax
# Class Name :
#      Constructor => Do Instantiation [ Create Instance From A Class ]
#      Each Instance Is Separate Object
#      def __init__(self, Other_data)
#          Body Of Function


class Member :
    
    def __init__(self):
        
        print("A NEw Member Has Been Added")
        
    
Member()
Member()
Member()

# print(dir(str))

member_one = Member()
member_two = Member()
member_three = Member()

print(member_one.__class__)


# my_dictionary = {
#     'name' : "osama",
#     'age'  : 36,
#     'monthly_salary' : 5000,
#     'yearly_salary' : ""   # something
# }

