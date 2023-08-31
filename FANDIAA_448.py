nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

def findDisappearedNumbers(nums):
    numSet = set()
    missingNums = []

    # Add each unique number in nums to the numSet
    for num in nums:
        numSet.add(num)

    # Check each number from 1 to n for missing numbers
    for i in range(1, len(nums) + 1):
        if i not in numSet:
            missingNums.append(i)

    return missingNums 

print(findDisappearedNumbers(nums))

# //  DRY RUN   //

# Initial state:
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# numSet = {}
# missingNums = []

# Iterating through nums:
# ------------------------
# num = 4
# numSet = {4}
# missingNums = []

# num = 3
# numSet = {3, 4}
# missingNums = []

# num = 2
# numSet = {2, 3, 4}
# missingNums = []

# num = 7
# numSet = {2, 3, 4, 7}
# missingNums = []

# num = 8
# numSet = {2, 3, 4, 7, 8}
# missingNums = []

# num = 2
# numSet = {2, 3, 4, 7, 8}
# missingNums = []

# num = 3
# numSet = {2, 3, 4, 7, 8}
# missingNums = []

# num = 1
# numSet = {1, 2, 3, 4, 7, 8}
# missingNums = []

# Finding missing numbers:
# ------------------------
# Checking 1: 1 exists in numSet
# Checking 2: 2 exists in numSet
# Checking 3: 3 exists in numSet
# Checking 4: 4 exists in numSet
# Checking 5: 5 does not exist in numSet, adding to missingNums
# Checking 6: 6 does not exist in numSet, adding to missingNums
# Checking 7: 7 exists in numSet
# Checking 8: 8 exists in numSet

# Final state:
# missingNums = [5, 6]


# By Anantia Keshri