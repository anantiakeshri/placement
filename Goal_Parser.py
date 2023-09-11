#1678 - Leet Code

command = "G()(al)"

def interpret(command): 
    s=""
    for i in range(len(command)):
        if command[i]=='G':
            s+=command[i]
        elif command[i]=='(' and command[i+1]==")":
            s+='o'
        elif command[i]=='(' and command[i+1]=='a':
            s+='al'
        else:
            pass
    print (s)
    
print(interpret(command))