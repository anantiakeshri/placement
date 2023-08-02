# Minimize Height II

k = 2
n = 4
arr = [1, 5, 8, 10]

# Output: 5
# Explanation:
# The array can be modified as {3, 3, 6, 8}. {(1+2)(5-2)(8-2)(10-2)}
# The difference between the largest and the smallest is 8-3 = 5.

def getMinDiff(arr, n, k):
    # code here
    arr.sort()
    diff = arr[n-1] - arr[0]
    sml = arr[0] + k
    tall = arr[n-1] - k
    
    for i in range(0,n-1):
        mi = min(sml,arr[i+1]-k)
        ma = max(tall,arr[i]+k)
        if mi < 0:
            continue
        else:
            diff = min(diff,ma-mi)
            
    return diff

print(getMinDiff(arr,n,k))

# for i in range(N):
#         if arr[i] <= 3:
#             arr[i] = arr[i] + K
#         else:
#             arr[i] = arr[i] - K
            
#     return arr