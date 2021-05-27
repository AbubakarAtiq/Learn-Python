print("\t----How do you call functions in Python?")
print("\tSimply write the function's name followed by 0,\n\tplacing any required arguments within the brackets.\n\tFor example, lets call the functions written above(in the previous example):\n\tf,f1,f2..")
def my_function():
    print("Hello from my functions!")
def my_function_with_args(usermane,greeting):
    print("Hello, %s, from my function!, I wish you %s"%(usermane,greeting))
def sum_two_numbers(a,b):
    return a+b
#Print (a simple greeting)
my_function()
#Prints - "Hello, John Doe, From my function!, I wish you a great year1"
my_function_with_args("John Doe","a great year!")
#after this line x will hold the value 3!
x=sum_two_numbers(1,2)