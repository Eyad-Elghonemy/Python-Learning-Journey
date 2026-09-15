# values = (0, 1, 2)

# if any(values):
  
#   # If At Least One Vlaue Is Fale == 0
  
#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# # my_list = [True, 1, 1, ["A", "B"], 10.5, 0]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

# # If All(['True', 1, 1, ["A", "B"]]) or all([True, 1, 1, ["A", "B"], 10.5, 0]) or all([True, 1, 1, ["A", "B"], 10.5, 0]) == True :


#   print("Good")

# else:

#   print("Bad")

# # Good

# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820

# for x in range(820) :
    
#     if sum(list(range(x+1))) == 820 :
        
#         print(x)




# 1 + 2 + 3 + 4 + ....... + 40 + 40 + (40 pow 40 % 40 ) 


# n = 20

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#   print("Good")

# Output => Good

# n = 1

# for x in range(100) :
    
#     i = list(range(n))
    
#     if round(sum(i) / n) == 10 :

#        print(n)
       
#        break
       
#     else :
        
#         n += 1


# def my_all(items) : 
    
#     k = 0 
    
#     for item in items :
        
#         if bool(item):
            
#             k += 1
            
#     if k == len(items) :
        
#         return "True"
    
#     else :
        
#         return "False"
    
    
    
# print(my_all([1, 2, 3])) # True
# print(my_all([1, 2, 3, []]))



# def my_any(items) : 
    
#     k = 0 
    
#     for item in items :
        
#         if bool(item):
            
#             k += 1
            
#     if k >= 1 :
        
#         return "True"
    
#     else :
        
#         return "False"
    
    
    
# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False


# def my_min(items) :
    
#     i = items[0]
    
#     for item in items :
        
#         if item < i :
            
#             i = item
            
#     return i
            
            


# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100



def my_max(items) :
    
    i = items[0]
    
    for item in items :
        
        if item > i :
            
            i = item
            
    return i



print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700