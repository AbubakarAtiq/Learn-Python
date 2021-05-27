#Accessing object functions
# To access a function inside of an object you use notation similar
# accessing a variable:#
class aclass:
    variable="This is a variable"
    def function(self):
        print("This is a message inside the class function.")
aobject=aclass()
aobject.function()