# Last updated: 3/31/2026, 9:39:48 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 1000000000
        maxdiff = -1
        for i in range(len(prices)):
            minn = min(minn, prices[i])
            maxdiff = max(maxdiff, prices[i]-minn)
        return maxdiff