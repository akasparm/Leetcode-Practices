"""Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray."""

nums = [2,3,-2,4]

curMaxValue, curMinValue = 1, 1
maxProduct = nums[0]

for num in nums:
    curMaxProduct = curMaxValue * num
    curMinProduct = curMinValue * num

    curMaxValue = max(curMaxProduct, curMinProduct, num)
    curMinValue = min(curMaxProduct, curMinProduct, num)

    maxProduct = max(maxProduct, curMaxValue)
print(maxProduct)