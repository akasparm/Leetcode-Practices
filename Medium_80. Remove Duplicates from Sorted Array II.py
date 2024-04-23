nums = [0,0,1,1,1,1,2,3,3]

j = 1
for i in range(1, len(nums)):
    if j == 1 or nums[i] != nums[j - 2]:
        nums[j] = nums[i]
        j += 1
print(j)

