# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

myskills = ["Html", "Css", "JS", "PHP"]

myskillswithcounter = enumerate(myskills, 20)

print(type(myskillswithcounter))

for counter, skill in myskillswithcounter :
    
    print(f"{counter} - {skill}")
    
print('#'*50)

# help()

# print(help(print))

print('#'*50)

# reversed(iterable)

mystrig = "Elzero"

print(reversed(mystrig))

for letter in reversed(mystrig) :
    
    print(letter)
    
print('#'*50)

my = ["Html", "Css", "JS", "PHP"]

# print(reversed(mystrig))

for s in list(reversed(my)) :
    
    print(s)