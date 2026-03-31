# Last updated: 3/31/2026, 9:38:29 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor = xor^n
        diff = xor & -xor
        u1 = 0
        u2 = 0
        for i in nums:
            if i&diff:
                u1 = u1^i
            else:
                u2 = u2^i
        return [u1,u2]