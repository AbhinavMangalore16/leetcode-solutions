# Last updated: 3/31/2026, 9:30:11 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxTriplet, maxElement, maxDiff = 0, 0, 0
        for num in nums:
            maxTriplet = max(maxTriplet, maxDiff * num)
            maxDiff = max(maxDiff, maxElement - num)
            maxElement = max(maxElement, num)
        return maxTriplet