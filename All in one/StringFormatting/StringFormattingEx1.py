#Python uses C-Style string formatting to create new, formatted 
# strings. The "%" operator is used to format a set of variables enclosed
# in a "tuple" (a fixed size list), together with a format string
# ,which contains normal text together with "argument specifers",
# special symbols like "%s" and "%d".
# Let's say you have a variable called "name" with your user name in
# it, and you would then like to
# print (out a greeting to that user.)#
#This prints out "Hello, johns!"
name="John"
print("Hello, %s!"%name)