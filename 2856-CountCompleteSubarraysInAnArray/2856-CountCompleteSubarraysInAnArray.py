# Last updated: 3/31/2026, 9:30:27 PM
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        res = 0
        for i in range(len(nums)):
            st = set()
            for j in range(i, len(nums)):
                st.add(nums[j])
                if len(st) == k:
                    res += 1
        return res