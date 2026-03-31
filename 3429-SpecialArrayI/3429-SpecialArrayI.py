# Last updated: 3/31/2026, 9:29:22 PM
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for index in range(len(nums) - 1):

                if ((nums[index] & 1) ^ (nums[index + 1] & 1)) == 0:
                    return False
        return True  