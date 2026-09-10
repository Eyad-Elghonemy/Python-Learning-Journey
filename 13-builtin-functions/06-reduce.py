# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On First And Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fourth Element And So On
# [5] Till One Element Is left And This Is The Result Of the Reduce
# [6] The Function Can Be Pre-Defined Function Or Lambda Function
# ---------------------------------------------------------------

from functools import reduce


# def sumall(num1 , num2) :
    
#     return num1 + num2 

numbers = [1, 8, 2, 9, 100]

# result = reduce(sumall, numbers)

result = reduce(lambda num1 , num2 : num1 + num2, numbers)


print (result)

# ((((1 + 8) + 2) + 9) + 100)