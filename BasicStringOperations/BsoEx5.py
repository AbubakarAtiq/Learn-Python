astring="Hello world!"
print(astring[3:7])
#Ex6
print(astring[3:7:2])
#Ex7
print(astring[3:7])
print(astring[3:7:1])
#Ex8
#Result is !dlrow olleH#
#Note that both of them produce same output
# There is no function like strrev in C to reverse a string. But with
# the above mentioned type of slicw syntax you can easily reverse
# a string like this#
print(astring[::-1])
#Ex9
print(astring.upper())
print(astring.lower())
#Ex10
print(astring.startswith("Hello"))
print(astring.endswith("-Abubakar Atiq"))
#Ex11
afewwords=astring.split("")