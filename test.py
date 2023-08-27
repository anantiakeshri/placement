""" Args are tuple """
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        
print(add(70, 7, 70, 7))

""" Kwargs are Dict """
def cal(n, *args, **kwargs):
    print(n, args, kwargs)
    
cal(5, 3, 5, 9, x=10, y=30)
