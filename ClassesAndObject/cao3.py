#You can create multiple different objects that are of the same class
# (have the same variables and functions defined). However, each object contains 
# independent copies of the variables defined in the class. for instance, if we were
# to define another object with the "aclass" class and then change the string in the
# variable above:#
class aclass:
    variable="blah"
    def function(self):
        print("This is a message inside the class.")
myobjectx=aclass()
myobjecty=aclass()
myobjecty.variable="abubakar"
#Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)