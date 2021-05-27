#Removing a value
# to remove a specified index, use either one of the following
# notations:#
phonebook={
    "abubakar":3535,
    "atiq":4545,
    "butt":2525
}
del phonebook["butt"]
phonebook.pop("atiq")
print(phonebook)