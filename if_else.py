# // Check whether person is eligible for voting or not //
# Name = str(input())
# Age = int(input())

# if Age >= 18:
#     print("Eligible for voting")
# else:
#     print("Not eligible")


# // Check whether the number entered by user is even or odd
# Num = int(input("Enter the number: "))

# if Num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


# // Check whether the year is leap year or not
# year = int(input("Enter the year: "))

# if year%100 == 0:
#     if year%400 == 0:
#         print("Entered year is leap year: ", year)
#     else:
#         print("Not leap year")
# else:
#     if year%4 == 0:
#         print("Entered year is leap year - ", year)
#     else:
#         print("Not a leap year")


# // Write a program to accept a number between 1-12 and display name of the month and days in that month like 1 for Jan and num of days 31.. so on
Num = int(input("Enter number between 1 to 12: "))

if Num == 1:
    print("January")
    print("Number of days 31")
elif Num == 2:
    print("Feburary")
    print("Number of days in normal year is 28, else in leap year 29")
elif Num == 3:
    print("Mar")
    print("Number of days 31")
elif Num == 4:
    print("April")
    print("Number of days 30")
elif Num == 5:
    print("May")
    print("Number of days 31")
elif Num == 6:
    print("June")
    print("Number of days 30")
elif Num == 7:
    print("July")
    print("Number of days 31")
elif Num == 8:
    print("Aug")
    print("Number of days 31")
elif Num == 9:
    print("Sept")
    print("Number of days 30")
elif Num == 10:
    print("Oct")
    print("Number of days 31")
elif Num == 11:
    print("Nov")
    print("Number of days 30")
elif Num == 12:
    print("Dec")
    print("Number of days 31")
else:
    print("Number from 1 to 12")
























