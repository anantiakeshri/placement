# Printing even number from 0 to 1000

even_number = 0
for even in range(0, 1001, 2):
    even_number += even
    
print(even_number)