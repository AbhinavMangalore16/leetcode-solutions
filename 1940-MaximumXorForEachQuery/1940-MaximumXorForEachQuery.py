# Last updated: 3/31/2026, 9:33:32 PM
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        XOR = nums[0]
        maxXor = (1<<maximumBit) -1

        for i in range(1,len(nums)):
            XOR ^= nums[i]

        ans = []
        for i in range(len(nums)):
            ans.append(XOR ^ maxXor)
            XOR ^= nums[len(nums)-i-1]
        return ans