def groupAnagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())

 
def get_input():
    print("Please enter the strings separated by spaces:")
    input_strs = input().split()
    return input_strs

input_strs = get_input()
output = groupAnagrams(input_strs)
print("Grouped anagrams:")
for group in output:
    print(group)
