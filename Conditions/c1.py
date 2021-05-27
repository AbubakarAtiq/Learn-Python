#Notice that variable assignment is done using a single equals 
# operator "=", whereas comparison between two variables is done
# using the double equals operator "==". The "not equals" operator
# is marked as"!="#.
#Boolean operators
# The "and" and "or" boolean operators allow building complex
# boolean expressions, for example:
# #
name="John"
age=23
if name=="John" and age==23:
    print("Your name is John, and you are also 23 years old")
if name=="John" or name=="Rick":
    print("your name is either John or Rick.")