
S = 'programming'

# def isPalindrome(S):
#     if S == S[::-1]:
#         return 1
#     else:
#         return 0

# print(isPalindrome(S))

def palindrome(S):
    i = 0
    j = len(S) - 1
    while (i < j):
        if S[i] != S[j]:
            return 0
        i = i + 1
        j = j - 1
        return 1
    
print(palindrome(S))