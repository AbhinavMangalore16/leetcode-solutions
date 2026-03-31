# Last updated: 3/31/2026, 9:34:16 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1) 