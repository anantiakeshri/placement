# Factorial of a number

num = int(input("Enter the number: "))
fact = 1

for i in range(2, num+1):
    fact = fact * i
print(fact) 