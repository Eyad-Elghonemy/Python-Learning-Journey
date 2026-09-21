# -------------------------------------------------
# Regular Expressions => Re Module Split And Sub --
# -------------------------------------------------
# split(Pattern, String, Maxsplit)  => Return A List Of Elements Splitted On Each Match
# Sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ----------------------------------------------------------------


import re 


string_one = "i Love Python Programming Language"

search_one = re.split(r"\s",string_one,1)

print(search_one)

print('#'*50)

string_two = "How-To_write_A_Very-Good-Article"

search_two = re.split(r"-|_",string_two)

print(search_two)

print('#'*50)

# Get Words From URL

for counter, word in enumerate(search_two) :
    
    if len(word) != 1 :
    
        print(f"word Number : {counter} => {word.lower()}")
        
    else :
        
        continue
    
print('#'*50)

print(re.sub(r"\s", "-", "I Love Python" , 1))