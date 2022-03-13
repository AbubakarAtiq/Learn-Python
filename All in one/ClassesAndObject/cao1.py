#we will explain why you have to include that "self" as a parameter
# a little bit later. First, to assign the above class(template) to 
# an object you would do the following:#
class aclass:
    variable="blah"
    def function(self):
        print("This is a message inside the class.")
aobject=aclass()
#   Now the variable "aobject" holds an object of the class "aclass"
# that contains the variable and the function defined within the class
# called "aclass".#
