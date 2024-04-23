nums = [1,3,4,2]
target = 6

num_indices = {}
for i, num in enumerate(nums):
    print("Num_indices: ", num_indices)
    complement = target - num
    if complement in num_indices:
        print([num_indices[complement], i])
    num_indices[num] = i
