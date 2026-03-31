# Last updated: 3/31/2026, 9:36:02 PM
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = 0
        ps = 0
        d = {0:1}
        for i in nums:
            ps+=i
            mod = ps%k
            if mod<0:
                mod+=k
            if mod in d:
                c += d[mod]
                d[mod] +=1
            else:
                d[mod] = 1
        return c