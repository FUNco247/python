from typing import Tuple


# super minimal recap of types in python

a_string = "recap python"
a_number = 3
a_float = 3.12 # number type and float type is different in python
a_boolean = True # True & False should be start with uppercase
a_none = None # start with uppercase & mean null

a_list = ["can", "I", "be", "BA", "?"] # list in python is mutable sequence
print("I" in a_list) # True

a_list.append("yes")
print(a_list) # ["can", "I", "be", "BA", "?", "yes"]

a_list.reverse()
print(a_list) # ['yes', '?', 'BA', 'be', 'I', 'can']

a_tuple = ("I", "can", "do") # unmutable sequence
# a_tuple.append("!") => error ! 'tuple' object has no attribute 'append'
print(a_tuple)

a_object = {
    "name" : "don't know",
    "age" : "secret",
    1 : "one"
}
print(a_object)

