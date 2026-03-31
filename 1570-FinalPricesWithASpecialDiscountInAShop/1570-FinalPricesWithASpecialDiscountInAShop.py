# Last updated: 3/31/2026, 9:34:26 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]: 
        result = prices.copy()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
        return result