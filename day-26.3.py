# Dictinoary Comprehension

""" Making a new dict containing name and random score generated using random """
import random
# new_dict = {new_key:new_val for item in list}
names = ['Anantia', 'Sagar', 'Radhika', 'Shally', 'Aryan', 'Princi', 'Yaseen', 'Sanchita', 'Santhu']

new_dict = {student:random.randint(1, 100) for student in names}
print(new_dict)


""" A dict comprehension in another dict using condition """
# passed_student = {new_key:new_val for (key, val) in dict.item() if test}

passed_student = {student:score for(student, score) in new_dict.items() if score >= 60}
print(passed_student)


""" Dictionary Comprehension to create a dictionary called result,
    that takes each word in the given sentence and calculates the number of letters in each word."""
# result = {new_key:new_val for item in list}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


""" Dictionary Comprehension to create a dictionary called weather_f 
    that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit."""
# weather_f = {new_key:new_val for (key, val) in dict.item() if test}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {days: (temp_c * 9/5) + 32 for (days, temp_c) in weather_c.items()}
print(weather_f)


