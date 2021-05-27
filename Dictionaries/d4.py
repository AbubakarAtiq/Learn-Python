#Exercise
# Add "Jake" to the phonebook with the phone number 03219470315,
# and remove Jill from the phonebook.#
phonebook={
    "a":1,
    "b":2,
    "c":3
}
phonebook["b"]=3219470315
del phonebook["c"]
if "b" in phonebook:
    print("b is listed in the phonebook.")
if "c" not in phonebook:
    print("c is not listed in the phonebook.")
if "a" in phonebook:
    print("This is abubakar atiq number, Trust me")