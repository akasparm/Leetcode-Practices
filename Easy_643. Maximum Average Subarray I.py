class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_window_avg = sum(nums[:k])/k
        final_window_avg = temp_window_avg

        i = k
        while i<len(nums):
            temp_window_avg = temp_window_avg - nums[i-k]/k + nums[i]/k
            # print(final_window_avg, temp_window_avg)
            if final_window_avg < temp_window_avg:
                 final_window_avg = temp_window_avg
            i+=1
    
        return final_window_avg