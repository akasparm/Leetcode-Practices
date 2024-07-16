"""
We keep on expanding the window as long as k is not negative , but the moment k becomes negative we start contracting the window from left while still expanding from right . It will look like shifting the whole window to the right. If k becomes zero at some point then we again stop contracting the window .this way we get max window with at max k extra zeroes.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

############################ From Solutions ##############################

        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1