# From solutions

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k=len(nums)
        j=[1]*k
        pre=1
        post=1
        for i in range(k):
            j[i]*=pre
            pre = pre*nums[i]
            j[k-i-1]*=post
            post=post*nums[k-1-i]
        return(j)