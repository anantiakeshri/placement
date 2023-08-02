intervals = [[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start value
    res = []  # Resultant list to store merged intervals

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)  # Add interval to the result if it doesn't overlap
        else:
            res[-1][1] = max(res[-1][1], interval[1])  # Merge overlapping intervals

    return res

print(merge(intervals))
    

