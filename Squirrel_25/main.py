# importing pandas library
import pandas

# reading CSV file
data = pandas.read_csv("Squirrel_25/Squirrel_Data.csv")

# finding count of gray squirrel
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)

# finding count of cinnamon squirrel
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_squirrels_count)

# finding count of black squirrel 
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

"""Creating a new data frame from scratch"""
# Creating new dict
new_squirrel = {
    "Fur Color" : ['Gray', 'Cinnamon', 'Black'],
    "Count" : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# Converting new_squirrel to pandas DataFrame
new_data = pandas.DataFrame(new_squirrel)

# Converting it to CSV file
new_data.to_csv("Squirrel_25/My_squirrel_data.csv")