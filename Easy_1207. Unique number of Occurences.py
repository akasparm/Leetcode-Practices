class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = dict()
        
        for a in arr:
            try:
                arr_dict[a] += 1
            except:
                arr_dict[a] = 1
            print(arr_dict)
            
        temp_list = []
        for a in arr_dict:
            if arr_dict[a] in temp_list:
                return False
            temp_list.append(arr_dict[a])
    
        return True
    
##################### From Solutions #####################

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         freq = {}
#         for x in arr:
#             freq[x] = freq.get(x, 0) + 1   # If x is not found in the dictionary, it returns the default value as 0.

#         return len(freq) == len(set(freq.values()))