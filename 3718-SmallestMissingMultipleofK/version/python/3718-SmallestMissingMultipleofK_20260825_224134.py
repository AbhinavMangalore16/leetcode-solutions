# Last updated: 8/25/2026, 10:41:34 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        s = set(nums)
4        mul = k
5        while mul in s:
6            mul+=k
7        return mul