#   can we use "else" clause for loops?     #
# Unlike languages like C, CPP. We can use else for loops. When the
# loop condition of "for" or "while" statement fails then code part
# in "else" is executed. if a break statement is executed inside the
# for loop then the "else" part is skipped. Note that the "else"
# part is executed even if there is a continue statement.
# Here are a few examples:
# Prints out 0,1,2,3,4 and then it prints "count value reached 5#
count=0
while(count<5):
    print(count)
    count+=1
else:
    print("Count value reached %d"%(count))
#prints out 1,2,3,4
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because"
    "of break but not due to fail in condition")