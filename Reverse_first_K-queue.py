from collections import deque

def reverseFirstK(q, k):
    s = len(q) - k
    for _ in range(s):
        x = q.popleft()
        q.append(x)
        
    return q

k = 4
q = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  


print("Queue before reversing :")
print(q)  

print("Queue after reversing :")
print(reverseFirstK(q, k))