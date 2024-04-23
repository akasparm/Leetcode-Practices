class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        return nums
    
def main():
    instance = Solution()
    print(instance.rotate(nums = [-1,-100,3,99], k = 2))


if __name__=="__main__":
    main()
