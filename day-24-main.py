# file = open('day-24.txt')

# contents = file.read()
 
# print(contents)

# file.close()

# with open('day-24.txt', mode="a") as file:
#     file.write("\nMy favourite food is Pasta.")

# By default mode stays in read.
with open('day-24.txt') as file:
    contents = file.read()    
    print(contents)