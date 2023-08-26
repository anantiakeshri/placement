# List Comprehension
# new_list = [new_item for item in list]
""" Working with numbers"""
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

""" Working with String"""
name = "Anantia"
new_str = [letter for letter in name]
print(new_str)

""" Creating a list from a range, where the list items are double the value in the range"""
# O/P : [2, 4, 6, 8]
new_number = [n*2 for n in range(1, 5)]
print(new_number)


## CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]

""" Create a list, new_names from names where name of person is longer than 5 letters """
names = ["Anantia", "Radha", "Yash", "Sagar", "Siddharth", "Harsimran", "Aryan"]
new_name = [name.upper() for name in names if len(name) > 5 ]
print(new_name)