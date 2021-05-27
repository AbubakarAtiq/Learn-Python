#Any object which is not a string can be formatted using the %s
# operator as well. THe string which returns from the "repr" method
# of that object is formatted as the string. For example:
mylist=[1,2,3]
print("A list: %s"%mylist)
#Here are some basic argument specifiers you should know:
#
# %s- String (or any object with a string representation, like number
# %d- Integers
# %f - floating point numbers
# _<number of digits>f- Floating point numbers with a fixed amount of digits
# to the right of the dot.
# %x/%x - Integers in hex representation (upper/lowercase)#