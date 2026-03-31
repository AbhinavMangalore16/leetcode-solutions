# Last updated: 3/31/2026, 9:34:17 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        good = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                good = good + d[nums[i]]
                d[nums[i]] +=1
        return good