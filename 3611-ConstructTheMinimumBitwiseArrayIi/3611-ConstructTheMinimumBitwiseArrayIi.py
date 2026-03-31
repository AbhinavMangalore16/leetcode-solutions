# Last updated: 3/31/2026, 9:28:55 PM
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, v in enumerate(nums):
            res[i] = -1 if v == 2 else self._calc(v)
        return res

    def _calc(self, value):
        bits_on_right = 0
        v = value
        while (v & 1) != 0:
            bits_on_right += 1
            v >>= 1
        if bits_on_right == 1:
            return value - 1
        wo_bits_on_right = value ^ ((1 << bits_on_right) - 1)
        return wo_bits_on_right | ((1 << (bits_on_right - 1)) - 1)
        