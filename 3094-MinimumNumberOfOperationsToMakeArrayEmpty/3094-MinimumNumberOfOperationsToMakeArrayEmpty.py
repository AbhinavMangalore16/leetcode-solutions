# Last updated: 3/31/2026, 9:30:14 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        opns = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        for i in d.values():
            if i==1:
                return -1
            opns += i//3
            if (i%3):
                opns+=1
        return opns    