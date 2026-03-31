# Last updated: 3/31/2026, 9:41:25 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashmap:
                return [i, hashmap[x]]
            hashmap[nums[i]] = i
        return []
            