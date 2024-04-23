nums = [-2,1,-3,4,-1,2,1,-5,4]
max_current = max_global = nums[0]
for num in nums[1:]:
    print("Num: ", num)
    print("before: ",max_current, max_global)
    max_current = max(num, max_current + num)
    max_global = max(max_global, max_current)
    print("After: ",max_current, max_global)
