""" QUESTION :- 
Sumit was cleaning his house and found an old book of math problems. In one of the pages was given a set of numbers with some digits missing 
The places where the digits were missing were indicated with (an underscore). At the end of the page was a clue to fill in the missing digits 
"All these numbers are perfect square Following the clue, Sumit wants to identify the largest perfect square that matches the pattern on that page. 
Can you help him with a program to do so? """

# Constraints:
# Length of the pattern, P<=13

# Input1 = 1_0_5
# Sample Output1: 11025
# Explanation: Here, 11025 matches the pattern 1.05 and is the largest perfect square: So, it will print 11025 as an output

# Input2 = 12_4_9
# Sample Output2: 127449
# Explanation: Here two numbers 120409 and 127449, watch the input pattern 12_4_9 and, out of these, 
# the largest perfect squares 127449, 50, it wil print 127442 as an output

def is_perfect_square(num):
    # made a sqrt function because of not using MATH library
    # Check if a number is a perfect square using integer arithmetic
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

def ResultantString(s):
    max_num = int("9" * len(s))  # Calculate the maximum number with the same number of digits as the pattern
    largest_perfect_square = -1

    for num in range(max_num, 0, -1):
        if is_perfect_square(num):
            # Check if the squared number matches the pattern by converting both to strings
            num_str = str(num)
            if len(num_str) == len(s):
                matches = True
                for i in range(len(s)):
                    if s[i] != '_' and s[i] != num_str[i]:
                        matches = False
                        break
                if matches:
                    largest_perfect_square = max(largest_perfect_square, num)

    return largest_perfect_square

def main():
    # Input1 = "1_0_5"
    Input2 = "12_4_9"
    result = ResultantString(Input2)
    print(result)
    
main()