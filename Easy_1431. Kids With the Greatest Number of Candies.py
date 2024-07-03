class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)

        for index, i in enumerate(candies):
            if i + extraCandies >= max_cand:
                candies[index] = True
            else:
                candies[index] = False

        print(candies)
        return candies
            