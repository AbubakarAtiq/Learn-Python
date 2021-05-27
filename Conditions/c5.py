#A statement is evaluated as true if one of the following is correct:
# 1. The "True" boolean variable is given, or calculated using an expression, such as 
# an arithmetic comparison.
# 2. An object which is not consider "Empty" is passed 
# Here are some examples for objects which are considered as empty: 
# 1. An empty string:
# 2. An empty list[].
# 3. The number zero:0
# 4. The false boolean variable: False#
#   The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match the values of
# the variables, but the instances themselves. For example:
# #
x=[1,2,3]
y=[1,2,3]
print(x==y)#Prints out True
print(x is y)#Print out False by Definition