# // WAP a prog to print first 10 natural number using loop
# for i in range(1, 11):
#     print(i)
       
# i = 1
# while i <= 10:
#     print(i) 
#     i += 1

# // Print number pattern 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# print("Number Pattern ")
# row = 8
# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")

# print("Number Pattern")
# n = int(input('Enter number of rows : '))
# i = 1
# while i <= n :
#     j = 1
#     while j <= i:
#         print(j, end = " ")
#         j += 1
#     print()
#     i += 1


# // Calculate the sum of all numbers from 1 to a given number.
n = int(input("Enter any number: "))
s = 0
for i in range(1, n+1, 1):
    s += i
    
print("Sum of n number is: ", s)
    