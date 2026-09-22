# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://WWW.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search("(https?)://(WWW)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)?", my_web)

# print(search.group(1))

# print('#'*50)

# print(search.groups())

# for group in search.groups() :
    
#     print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")


# Ignore Case In Pythex  ## A=a  (I)

# Verbose In Pythex  ## Let You Write Comment In It (#)  (V)

# Dot All (\.)  (Match Everything Including New Line) (D)

# Multi line  (M)

