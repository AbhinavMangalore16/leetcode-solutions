# Last updated: 3/31/2026, 9:35:50 PM
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxleft = [0]*len(values)
        maxleft[0] = values[0]
        maxx = 0
        for i in range(1, len(values)):
            curr = values[i] - i
            maxx = max(maxx, maxleft[i-1]+curr)
            curr = values[i] + i
            maxleft[i] = max(maxleft[i-1], curr)
        return maxx