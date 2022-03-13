# Exercise
# The target of this exercise is to create a string, an integer, and a floating point number.
#  The string should be named mystring and should contain the word "hello".
#  The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
#change this code
mystring="hello"
myfloat=10.0
myint=20
#Testing code
if mystring=="hello":
    print("String:%s" %mystring)
if isinstance(myfloat,float) and myfloat==10.0:
    print("Float: %f" %myfloat)
if isinstance(myint,int) and myint==20:
    print("Integer: %d" %myint)
#
# you can learn about the isinstance function from this
# link https://linuxhint.com/python_isinstance_function/#:~:text=The%20isinstance%20%28%29%20function%20is%20a%20built-in%20function,%28%29%20function%20with%20the%20help%20of%20simple%20examples.#
