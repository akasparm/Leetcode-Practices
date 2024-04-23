nums = [1,5,-2,-4,0]
nums_set = set(nums)
nums.sort()
nums_og_sorted = list(nums_set)
nums_og_sorted.sort()
if nums_og_sorted == nums:
    print(False)
print(True)