# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()   => Search A String For A Match And Return A First Match Only
# findall()  => Returns A List Of All Matches And Empty List If No Match
# ---------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net)
# ---------------------------------------------------------

import re

# my_string = re.search(r"[A-Z]{2}", "OSamaElzero")

# print(my_string.span())
# print(my_string.string)
# print(my_string.group())



# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

# if is_email :
    
#     print("Print This Is A Valid Email")
#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())
    
    
# else :
    
#     print("Print This Is Not A Valid Email")
    
    
email_input = input("Please Write Your Email :")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)  # if in group Return it only

empty_list = []

if search != [] :
    
    empty_list.append(search)
    
    print("Email Added")
    
else :
    
    print("Invalid Email")
    
for email in empty_list :
    
    print(email)