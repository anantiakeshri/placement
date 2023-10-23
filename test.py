
""" Arguments are tuple """
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        
print(add(70, 7, 70, 7))

""" Kwargs are Dictionary """
def cal(*args, **kwargs):
    print(args, kwargs)
    
cal(3, 5, 9, x=10, y=30)