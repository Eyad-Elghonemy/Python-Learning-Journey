# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Beacause It Map The Functions On Every Element
# [3] The Function Can  Be  Pre-Defined Function Or Lambda Function
# -----------------------------------------------------------------

# USe Map With PreDefined Function

def formattext(text) :
    
    return f"- {str(text).strip().capitalize()} -"

mytexts = [" Osama ", " Ahmed ", " Sayed "]

# myformateddata = map(formattext, mytexts)

# print(myformateddata)

for name in  list(map(formattext, mytexts)) :
    
    print(name)
    
    
print('#'*50)
    
    
# USe Map With Lambda Function

# def formattext(text) :
    
#     return f"- {str(text).strip().capitalize()} -"

mytexts = [" Osama ", " Ahmed ", " Sayed "]

for name in  list(map( lambda text : f"- {str(text).strip().capitalize()} -" , mytexts)) :
    
    print(name)
    
print('#'*50)