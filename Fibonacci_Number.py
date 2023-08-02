#Fibonacci_Number using Dynamic Programming
#Dynamic Programming

# def fibo(number):
#     number1 = 0
#     number2 = 1
    
#     if number < 0:
#         print("Incorrect number")
#     elif number == 0:
#         return number1
#     elif number == 1:
#         return number2
#     else:
#         for i in range(2, number+1):
#             Z = number1 + number2
#             number1 = number2
#             number2 = Z
#         return number2
    
# print(fibo(12))


#2nd Solution
# Fibonacci Series using Dynamic Programming
# def fibonacci(n):
    
# 	# Taking 1st two fibonacci numbers as 0 and 1
# 	f = [0, 1]

# 	for i in range(2, n+1):
# 		f.append(f[i-1] + f[i-2])
# 	return f[n]

# print(fibonacci(9))

#3rd solution to print Series of Fibonacci Number
n = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
next_number = 0
count = 1

while(count <= n):
	print(next_number, end=" ")
	count += 1
	num1 = num2
	num2 = next_number
	next_number = num1 + num2
	t_number = num1 + num2
 




