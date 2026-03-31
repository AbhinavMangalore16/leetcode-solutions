# Last updated: 3/31/2026, 9:35:13 PM
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        cnt[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += cnt[t - k]
            cnt[t] += 1
        return ans        