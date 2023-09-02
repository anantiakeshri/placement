height = [1,8,6,2,5,4,8,3,7]                #Input

# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

def maxArea(height):
    # LINEAR SOLUTION   O(n)
    res = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res

print(maxArea(height))