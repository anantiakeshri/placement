
string = 'ABCDCDC'
sub_string = 'CDC'

def count_substring(string, sub_string):
    count = 0
    ml = len(string)
    sl = len(sub_string)
    
    for i in range(ml-sl+1):
        if (string [i:(i+sl)] == sub_string):
            count = count +1
    return count
    
print(count_substring(string, sub_string))
