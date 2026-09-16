# def remove_chars(name) :
    
#     return name[1:-1]
    
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list = list(map(remove_chars, friends_map))

# for s in cleaned_list :
    
#     print(s)
    
# print('$'*60)

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# for s in  list(map( lambda name : name[1:-1] , friends_map)):
    
#     print(s)

print('$'*60)

# def get_names(name) :
    
#     return str(name).endswith("m")

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


# names = list(filter(get_names, friends_filter))

# for text in names :
    
#     print(text)



# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# for text in list(filter(lambda name : str(name).endswith("m") , friends_filter)) :
    
#     print(text)

# nums = [2, 4, 6, 2]

# def multi(*numbers):
    
#     return numbers[0] * numbers[1]

# from functools import reduce 

# result = reduce(multi, nums)

# print(result)

# nums = [2, 4, 6, 2]

# from functools import reduce 

# result = reduce(lambda *numbers : numbers[0] * numbers[1], nums)

# print(result)

# skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# myskillscounter = enumerate(reversed(skills),50)

# for c, s in myskillscounter :
    
#     if type(s) == int :
        
#         continue
    
#     else:
        
#         print(f"{c} - {s}")

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

d = skills[::-1]

myskillscounter = enumerate(d,50)

for c, s in myskillscounter :
    
    if type(s) == int :
        
        continue
    
    else:
        
        print(f"{c} - {s}")