#Sorting array without built in function
#drawback TLE

nums = [5, 1, 2, 0, 0, 2]
nums1 = []

def sortArray(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(sortArray(nums))