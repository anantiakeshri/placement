#Kadane's Algorithm

N = 5
arr = [1,2,3,-2,5]

def Kadane(arr, N):
    max = -99999999999
    sum_subarr = 0
    
    for i in range(N):
        sum_subarr = sum_subarr + arr[i]
        if sum_subarr > max:
            max = sum_subarr
        
        if sum_subarr < 0:
            sum_subarr = 0
            
    return max

print(Kadane(arr,N))