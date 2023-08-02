# def reverseArr(arr,start,end):            #Recursive Way - O(n)
#     if start >= end:
#         return
#     arr[start], arr[end] = arr[end], arr[start]
#     reverseArr(arr, start+1, end-1)

# arr = [1, 2, 3, 4, 5, 6]
# print(arr)
# reverseArr(arr, 0, 5)
# print("Reversed list is")
# print(arr)

def reverseArr(arr, start, end):                    #Iterative way - O(n)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
arr = [18, 12, 6, 22, 9, 20]
print(arr)
reverseArr(arr, 0, 5)
print("Reversed list is")
print(arr)