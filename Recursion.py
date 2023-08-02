
def natural(n):
    if n <= 0:
        return
    print(n,end=" ")
    natural(n-1)
    
natural(20)