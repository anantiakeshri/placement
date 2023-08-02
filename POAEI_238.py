nums = [1,2,3,4]
# Output: [24,12,8,6]

#Explanation: multiply 2*3*4 = 24 except 1 | 1*3*4 = 12 | 1*2*4 = 8 | 1*2*3 = 6.

def productExceptSelf(nums):
    res = [1] * (len(nums))                     # Create a result array filled with 1s
    
    prefix = 1                                  # Initialize a variable to store the prefix product
    for i in range (len(nums)):         
        res[i] = prefix                         # Store the prefix product at the current index in the result array
        prefix *= nums[i]                       # Update the prefix product by multiplying with the current number
        
    postfix = 1                                 # Initialize a variable to store the postfix product
    for i in range (len(nums) -1, -1, -1):
        res [i] *= postfix                      # Multiply the current element in the result array with the postfix product
        postfix *= nums[i]                      # Update the postfix product by multiplying with the current number

    return res

print(productExceptSelf(nums))