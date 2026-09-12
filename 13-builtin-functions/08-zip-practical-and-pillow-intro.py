# ----------------------------------------------------
# -- Practical => Loop On Many Iterators With zip() --
# ----------------------------------------------------
# zip() Return A zip Object Contains All Objects
# zip() Length Is The Length Of Lowest Object 
# ------------------------------------------------
 
list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C','D']
tuple1 = ("Man", "Women", "Girl", "Boy")
dict1 = {"Name" : "Osama", "Age" : 36, "Country" : "Egypt", "Skill" : "Python"}


for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    
    print("List 1 Item =>", item1)
    print("List 2 item =>", item2)
    print("Tuple 1 item =>", item3)
    print("Dict 1 Key =>", item4, "Value =>", dict1[item4])

# ultimatelist = zip(list1,list2)

# print(ultimatelist)

# for item in ultimatelist :
    
#     print(item)


from PIL import Image

myimage = open(r"C:\Users\eyad0\OneDrive\Pictures\Screenshots\elzero-pillow.png")

