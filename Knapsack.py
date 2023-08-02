def knapSack(W, wt, val, n):
	# Base Case                                         # val = profit from object, n = number of element
	if n == 0 or W == 0:                                # W = Weight of Bag, wt = weight of object 
		return 0

	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included     (2) not included
	else:
		return max(val[n-1] + 
            knapSack(W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))


# Driver Code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	print (knapSack(W, weight, profit, n))

