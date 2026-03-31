# Last updated: 3/31/2026, 9:29:59 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        left = 0
        maxiOccurence = 0
        res = 0
        for right in range(len(nums)):
            maxiOccurence += nums[right] == maxi
            while maxiOccurence >= k:
                maxiOccurence -= nums[left] == maxi
                left += 1
            res += left
        return res