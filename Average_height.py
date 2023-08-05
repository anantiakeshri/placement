# Calculating Average height without using sum() and len() function

student_heights = input("Input a list of student heights: \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height 
print(f"Sum of heights: {total_height}")

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(f"Number of students : {number_of_student}")

average_height = round(total_height / number_of_student)
print(f"Average height: {average_height}")


# Anantia Keshri