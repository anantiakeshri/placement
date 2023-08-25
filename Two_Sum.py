nums = [2,7,11,15] 
target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return([seen[target - num], i])
        
        elif num not in seen:
            seen[num] = i
        
print(twoSum(nums, target))

# Explanation:
# Initial state: seen = {}
# Iteration 1:
# nums = [2, 7, 11, 15], target = 9
# seen = {}
#   i = 0, num = 2
#   target - num = 9 - 2 = 7
#   Store num = 2 as key and i = 0 as value in seen: {2: 0}

# Iteration 2:
# seen = {2: 0}
#   i = 1, num = 7
#   7 is present in seen as a key, so return [seen[7], i] (value corresponding to key 7 and current index)

# Final result: [0, 1]
