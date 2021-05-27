#"Break and continue" statements
# break is used to exist a for loop or a while loop, whereas continue
# is used to skip the current block, and return to the "for" or "While"
# statement. A few examples:
# prints out 0,1,2,3,4#
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break
#prints out only odd numbers - 1, 3, 5, 7, 8
for x in range(10):
    #check if x is even
    if x%2==0:
        continue
    print(x)