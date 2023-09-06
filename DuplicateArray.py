
# # arr = [12, 13, 14, 15, 16]
# # print(arr)

nums = [1,2,1,3,4,5,5]

def removeDuplicates(nums):
    # Create an empty set to store unique elements.
    unique_set = set()
    
    # Create a new list to store the unique elements in the order of appearance.
    unique_list = []
    
    for num in nums:
        if num not in unique_set:
            # If the element is not in the set, it's unique.
            # Add it to the set and the new list.
            unique_set.add(num)
            unique_list.append(num)
    
    # Copy the unique elements back to the original list if needed.
    # You can also return the unique_list if you don't want to modify the original list.
    nums[:] = unique_list
    
    # Return the length of the modified list with duplicates removed.
    return len(unique_list)

# Example usage:
nums = [1, 2, 1, 3, 4, 5, 5]
result = removeDuplicates(nums)
print(nums)  # The modified list with duplicates removed
print(result)  # The length of the modified list

