#Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. However, a
# dictionary, unlike a list, does not keep the order of the values
# stored in it. To iterate over key value pairs, use the following
# syntax:#
phonebook={"abubakar":6565,"atiq":4545,"butt":3232}
for name, number in phonebook.items():
    print("Phone number of %s is %d"%(name,number))