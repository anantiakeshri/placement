# # import os
# # print(os.getcwd())

# """Gave the absolute path because I was finding trouble"""
# # with open("C:/Users/anant/OneDrive/Desktop/Placement/day-25/weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)

# import csv

# with open('day-25\weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
# print(temperature)

""" How Much Time The Pandas Library Save Us ? """

import pandas

# """Gave the absolute path because I was finding trouble"""
# data = pandas.read_csv('day-25\weather_data.csv')

# # Print data as a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # Print Temperature as list
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Print average of temperature
# print(data["temp"].mean())

# # Print maximum temperature
# print(data["temp"].max())

# # Print or Get data as column - 2 ways method
# # print(data["condition"]) 
# print(data.condition)

# # Print data as Row
# print(data[data.day == "Thursday"])

# # PRINT ROW OF DATA WHICH HAS THE HIGHEST TEMP
# print(data[data.temp == data.temp.max()])


""" Creating a DataFrame from scratch"""
data_dict = { 
        "students" : ["Anantia", "Radhika", "Sagar"],           
        "scores" : [89, 90, 92]
}

data = pandas.DataFrame(data_dict)

# Converting data_dict to scv file
data.to_csv("day-25/new_data.csv")