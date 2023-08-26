# List Comprehension

""" Write a List Comprehension to create a new list called squared_numbers. 
    This new list should contain every number in the list numbers but each number should be squared."""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num*num for num in numbers]
print(squared_numbers)


""" Write a List Comprehension to create a new list called result. 
    This new list should only contain the even numbers from the list numbers."""
number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in number if num % 2 == 0]
print(result)


""" Take a look inside file1 and file2. 
    They each contain a bunch of numbers, each number on a new line.
    You are going to create a list called result which contains the numbers that are common in both files.
    The result should be a list that contains Integers, not Strings. """
    
file1 = ['1\n', '5\n', '10\n', '15\n', '20\n', '25\n', '30\n']
file2 = ['1\n', '2\n', '4\n', '6\n', '8\n', '10\n', '12\n', '14\n', '16\n', '18\n', '20\n']

result = [int(num) for num in file1 if num in file2]
print(result)