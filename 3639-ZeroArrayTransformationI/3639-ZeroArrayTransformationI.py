# Last updated: 3/31/2026, 9:28:48 PM
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(nums):
                diff[r + 1] -= 1
        cnt = 0
        for i in range(len(nums)):
            cnt += diff[i]
            if nums[i] > cnt:
                return False
        return True