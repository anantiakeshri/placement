from functools import reduce

""" MAP """
num = [1,2,3,4,5,6,7,8,9,10]
nums = list(map(lambda n : n*n, num))
print(nums)

""" REDUCE """
num = [1,2,3,4,5,6,7,8,9,10]
nums1 = reduce(lambda x,y: x+y, num)
print(nums1)

""" FILTER """
num = [4, 5, 6, 0, 34, 69, 10]
nums2 = list(filter(lambda x: x >= 10, num))
print(nums2)