# this is an exercise in which i have to make this program
# # "Hello.John. your current balance is $53.44"#
# data=("John","Doe",53.44)
# format_string=["hello","your current balance is $"]
# #print(format_string % data,"Your current balance is" %data[2])
# print(data[0])
# print(format_string[0],data[0],data[1],format_string[1],data[2])
#Above is my solution now i will write proper given solution
data=("John","Doe",53.44)
format_string="Hello %s %s. Your current balance is $%s."
print(format_string%data)