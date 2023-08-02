# Output: ["o","l","l","e","h"]

s = ["h", "e", "l", "l", "o"]

def reverseString(s):
    return s[::-1]

reversed_s = reverseString(s)
print(reversed_s)


# def reverseString(s):
#     i = 0
#     j = len(s)-1
    
#     while i<j:
#        s[i],s[j]=s[j],s[i]
#        i+=1
#        j-=1 
       
#     return s    # In Python, if a function does not explicitly return a value, it implicitly returns None by default.

# reversed_s = reverseString(s) 
# print(reversed_s)

# def reverseString(s):
#     print(s.reverse)
    
# print(reverseString(s))