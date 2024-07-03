# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:

#         i = nums.index(min(nums))
#         nums_copy = nums.copy()
#         while i<len(nums):
#             if nums[i]<=nums[i-1]:
#                 print(i)
#                 nums.pop(i-1)
#                 print(nums)
#                 i=1
#             else:
#                 i+=1
#             if len(nums)<3:
#                 return False
            
#         return True

################ FROM SOLUTIONS ################

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False

    