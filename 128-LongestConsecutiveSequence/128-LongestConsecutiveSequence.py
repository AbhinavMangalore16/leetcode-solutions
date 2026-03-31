# Last updated: 3/31/2026, 9:39:43 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for j in s:
            if j-1 not in s:
                c = 0
                while j+c in s:
                    c+=1
                m = max(c,m)
        return m

                    