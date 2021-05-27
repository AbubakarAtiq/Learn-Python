#
# Lists are very similar to arrays. 
# They can contain any type of variable, and they can contain as many variables as you wish.
# Lists can also be iterated over in a very simple manner. 
# Here is an example of how to build a list.#
mylist=[]
mylist.append(1)
#append means adding element in the list
mylist.append(2)
mylist.append(3)
print(mylist[0])#prints 1
print(mylist[1])#prints 2
print(mylist[2])#prints 3
#prints out 1,2,3
for y in mylist:
    print(y)