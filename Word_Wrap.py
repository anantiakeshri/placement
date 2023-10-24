# Word Wrap

n = 4
nums = [3,2, 2, 5]
k = 6

def solveWordWrap(nums, n, k):
	#Code here
	# A=nums                                  # A is copy of nums
    n=len(nums)
    dp=[float("inf")]*(n)                   #filling dp with infinity
    dp[-1]=0                                #filling last element of dp with 0 because last line will have no cost
        
    for i in range(n-2,-1,-1):              #traversing from second last element to first element
        length=-1                           #length of line
            
        for j in range(i,n):                #traversing from i to n of each word
            length+=nums[j]+1                  #adding length of each word and 1 for space

            if length<=k:
                if j==n-1:
                    cost=0
                else:
                    #cost of line
                    cost=(k-length)**2+dp[j+1]
            else:
                break
            dp[i]=min(dp[i],cost)
            
    return dp[0]
    
print(solveWordWrap)