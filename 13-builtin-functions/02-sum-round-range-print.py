# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum()
# sum(iterable, start)

a = [1, 10, 19, 40]

print(sum(a))
print(sum(a,40))

# round()

# round(number, num of digits)

print(round(150.499))
print(round(150.500))
print(round(150.501))
print(round(150.556, 2))

# range()

# range(start, end, step)  #مدي

print(list(range(0)))
print(list(range(10)))
print(list(range(0, 21 , 2)))

# print()
 
print("Hello  Osama How Are You")
print("Hello","Osama", "How", "Are", "You", sep="|")

print("Frist Line", end= " ")
print("Second Line")
print("third Line")