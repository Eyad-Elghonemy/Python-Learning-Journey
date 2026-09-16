# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#     my_data.extend(data)

# final_string = ("".join(my_data).title())
# print(final_string) # Elzero



# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    
#     my_data.append(item1)
#     if len(my_data) == len("Elzero") :
#         final_string = ("".join(my_data).title())

# print(final_string)



from PIL import Image 

my_box = (400,0,800,400)

myimage = Image.open(r"C:\Users\eyad0\OneDrive\Pictures\Camera Roll\elzero-pillow.png")

mynewimage = myimage.crop(my_box)

mynewimage.show()

myconvertedimg = mynewimage.convert("L")

myconvertedimg.show()

# myimage = Image.open(r"C:\Users\eyad0\OneDrive\Pictures\Camera Roll\elzero-pillow.png")

# my_box = (0,400,1200,800)

# mynewimg = myimage.crop(my_box)

# mynconvertimg = mynewimg.rotate(180).convert("L")

# mynconvertimg .show()


# def say_hello(name) :
    
#     """
#     parameter(someone) => Person Name
#     Function To Say Hello To Anyone
    
#     """
    
#     return f"Hello {name}"

# print(say_hello("Osama"))
# help(say_hello)

