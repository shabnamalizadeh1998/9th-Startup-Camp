def mergeIntervals(intervals):
   
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
       
        if not merged or merged[-1][1] < interval[0]:
            merged.append(list(interval))  
        else:

            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

def get_input():
    print("Please enter intervals in the format '(start, end)' separated by spaces:")
    input_intervals = input().strip().split()
    intervals = []
    for interval_str in input_intervals:
        start, end = map(int, interval_str.strip('()').split(','))
        intervals.append((start, end))
    return intervals

input_intervals = get_input()
merged_intervals = mergeIntervals(input_intervals)
print("Merged intervals:", merged_intervals)
