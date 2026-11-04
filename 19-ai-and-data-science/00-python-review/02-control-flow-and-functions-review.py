# is_student = False
# is_grad = False

# if(is_student):
#     print("Welcome Inside")
    

# elif(is_grad):
#     print("Congrats")   

# else : 
#     print("You Can't Go Ahead")

# print("Hello")

# is_man = True
# is_father = False


# if(is_man and not is_father):
#     print("Relative")
    
# else:

#     print("Not Relivant")

# is_grade = 10

# if(is_grade == 50):
#     print("A")
    
# elif(is_grade >= 30):
#     print("B")
    
# elif(is_grade < 30):
#     print("F")

# elif(is_grade != 0):
#     print("Exam Pass")

# else:
#     print("Good Luck")
    
# print("Exam Done")

# counter = 1

# while counter <= 4 : 
#     print("*")
#     counter += 1


# name = "OLA"

# for i in range(1, 20, 3) : 
#     print(i)

# [0,0]
# [0,1]
# [1,0]
# [1,1]

# for num1 in range(2):
#     for num2 in range(2):
#         print(f'{num1}, {num2}')

# num = 7

# count = 0
# while(count < 2):
#     guess_num = int(input("Enter Your Guess : "))
#     count += 1
#     if(guess_num == num):
#         print("Correct!!")
#         break
        
#     else:
#         print("Try Again")
        
# if(guess_num != num):
#     print("Your Tries Ended")


# msg = "Good Morning Python Learners"
# new_msg = ""

# for i in msg :
    
#     if(i.lower() == 'o'):
#        i = "0"
    
#     new_msg += i
        
# print(new_msg)
        
# def greeting(f_name, l_name):
#     print(f"Hello {f_name} {l_name}")
#     return None
    
    
# greet = greeting("Ola", "Ahmed")
# print(greet)

# def square(num):
#     return print(num * num)

# sq = square(2)
# print(sq)


#This Function Returns Numbers 0 OR 1
# def is_even(num):
    
#     return num % 2
    
# print(is_even(51))
 
def grad_in_percent(grade, fullmark):
    return (grade / fullmark)*100

gradPercent = grad_in_percent(34, 50)
print(f"The Grade is {gradPercent}%")