# Last updated: 3/31/2026, 9:39:37 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitCt = [0]*32
        for n in nums:
            for i in range(32):
                if n&(1<<i):
                    bitCt[i]+=1
        res = 0 
        for i in range(32):
            if bitCt[i]%3 != 0:
                res = res | (1<<i)
        if res>=2**31:
            res -=2**32
        return res