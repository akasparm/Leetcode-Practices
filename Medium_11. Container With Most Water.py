class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        capacity = 0

        while i != j:
            min_height = min(height[i], height[j])
            if capacity < (j - i)*min_height:
                capacity = (j - i)*min_height

            # print("i: ", i, "j: ", j)

            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            
            # print("Capacity: ", capacity)

        return capacity