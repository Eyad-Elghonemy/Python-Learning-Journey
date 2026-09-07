# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

# abs()

print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print('#'*50)

# pow(base, exp, mod) => Power

print(pow(2,5))     # 2 * 2 * 2 * 2 * 2

print(pow(2,5, 10))     # 2 * 2 * 2 * 2 * 2  % 10
 
print('#'*50)

# min(item, item, or iterator)

mynumbers = (1, 20, -50, -100, 100)

print(min(1, 10, -50, 20, 30))
print(min("A", "x", "Z", "Osama"))
print(min(mynumbers))

print('#'*50)

# max(item, item, or iterator)

mynumbers = (1, 20, -50, -100, 100)

print(max(1, 10, -50, 20, 30))
print(max("a", "x", "z", "osama"))
print(max(mynumbers))

print('#'*50)

# slice(start, end, step)

a = ["A", "B", "C", "D", "E", "F"]

print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
