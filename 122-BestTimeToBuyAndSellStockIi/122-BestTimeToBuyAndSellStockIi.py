# Last updated: 3/31/2026, 9:39:46 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                pr += (prices[i+1]-prices[i])
        return pr