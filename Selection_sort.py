# Follow the below steps to solve the problem:

# 1. Initialize minimum value(min_idx) to location 0.
# 2. Traverse the array to find the minimum element in the array.
# 3. While traversing if any element smaller than min_idx is found then swap both values.
# 4. Then, increment min_idx to point to the next element.
# 5. Repeat until the array is sorted.

# arr[] = {64, 25, 12, 22, 11}
# first pass - {11, 25, 12, 22, 64}
# second pass - {11, 12, 25,22, 64}
# third pass - {11, 12, 22, 25, 64}
# fourth pass - {11, 12, 22, 25, 64}

import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    minVal = i
    for j in range(i+1, len(A)):
        if A[minVal] > A[j]:
            minVal = j
            
    A[i], A[minVal] = A[minVal], A[i]
    
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")

            
        