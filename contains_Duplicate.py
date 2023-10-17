# Leet Code - Contains Duplicate

nums = [1,2,3,4,5,1,2,3]

def containsDuplicate(nums):
    return len(set(nums))!=len(nums)

    num_set = set()
    
    for i in nums:
        if i in num_set:
            return True
        else:
            num_set.add(i)
    return False

print(containsDuplicate(nums))