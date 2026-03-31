# Last updated: 3/31/2026, 9:34:33 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies
