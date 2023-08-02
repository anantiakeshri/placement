# Explanation: min = -4, max =  5. Sum = -4 + 5 = 1
# N = 1
# A = [8]

N = 5
A = [-5, 1, -4, 5, 3]

# def findSum(A,N): 
#     #code here
#     A.sort()                                # O(n log n)
#     if N == 1:
#         return A[0]*2
#     else:
#         return A[0]+A[-1]
        
# print(findSum(A,N))

def findSum(A,N):
    maxi = A[0]
    mini = A[0]
    for i in range(N):                         #O(n)
        if A[i] > maxi:
            maxi = A[i]
        if A[i] < mini:
            mini = A[i]
    return maxi + mini
        
print(findSum(A,N))