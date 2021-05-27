#What are functions
# Functions are a convenient way to divide your code into useful
# blocks, allowing us to order our code, make it more readable,
# reuse it and save some time. also functions are a key way to define
# interfaces so programmers can share their code.
# ------How do you write functions in python?
# As we have seen on previous tutorials, Python makes use of blocks.
# A block is a area of code of written in the format of:
# block_head:
#   1st block line
#   2nd block line
#   ...#
#where a block line is more Python code (even another block), and
# the block head is of the following format: block_keyword
# block_name(argument1,argument2,...)
# block keywords you already know are "if", "for", and "while".
# Functions in Python are defined using the block keyword "def",
# followed with the function's name as the blocks name. For example:
# #
def a_function():
    print("Hello from a function!")