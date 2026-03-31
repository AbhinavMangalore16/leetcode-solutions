# Last updated: 3/31/2026, 9:34:57 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            digits = 0
            while x > 0:
                digits += 1
                x //= 10
            if (digits & 1) == 0:
                count += 1
        return count