candidates = [2,3,6,7] 
target = 7
# Output: [[2,2,3],[7]]

# Explanation: 
# # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7. These are the only two combinations.

#candidates = [2,3,5]
# target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

def combinationSum(candidates, target):
    res = []
    for i in range (len(candidates)):
        
print(combinationSum(candidates, target))