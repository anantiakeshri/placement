nums = [1,2,3,4,5,1,2,3]

# print(len(nums))
# print(len(set(nums)))
# print(set(nums))

def containDuplicates(nums):
    num_set = []
    
    for i in nums:
        if i in num_set:
            return True
        else:
            num_set.add[i]
    return False
            
print(containDuplicates(nums))