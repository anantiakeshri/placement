
# # arr = [12, 13, 14, 15, 16]
# # print(arr)

nums = [1,2,1,3,4,5,5]

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0 
    
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1

print(removeDuplicates(nums))