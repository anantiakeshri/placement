def maxAmt( A, B):
    max_so_far = 0
    current_sum = 0
    for i in range(len(A)):
        current_sum += A[i]
        if current_sum > B:
            break
        else:
            max_so_far = max(max_so_far, current_sum)
    return max_so_far

if __name__ == "__main__":
  A = [1, 2, 3, 4, 5]
  B = 10
  print(maxAmt(A, B))