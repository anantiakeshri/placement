x = -121
# Output: false

def isPalindrome(x):
    if x < 0:
        return False
    else:
        x_str = str(x)
        i = 0
        j = len(x_str) - 1
        for _ in range(len(x_str)):
            if x_str[i] != x_str[j]:
                return False
            i = i + 1
            j = j - 1
        return True
    
print(isPalindrome(x))