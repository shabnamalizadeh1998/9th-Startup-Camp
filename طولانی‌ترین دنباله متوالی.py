def longestConsecutive(nums):
    num_set = set(nums)
    max_length = 0
    longest_sequence = []
    
    for num in nums:
        if num - 1 not in num_set:  
            current_num = num
            current_length = 1
            current_sequence = [num]
            
            while current_num + 1 in num_set:   
                current_num += 1
                current_length += 1
                current_sequence.append(current_num)
            
            if current_length > max_length:
                max_length = current_length
                longest_sequence = current_sequence
            
    return max_length, longest_sequence

 
def get_input():
    print("Please enter the numbers separated by spaces:")
    input_nums = list(map(int, input().split()))
    return input_nums


input_nums = get_input()
result_length, result_sequence = longestConsecutive(input_nums)
print("Length of the longest consecutive sequence:", result_length)
print("Longest consecutive sequence:", result_sequence)
