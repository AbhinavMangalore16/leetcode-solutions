# Last updated: 3/31/2026, 9:29:26 PM
class Solution:
    def minOperationsToMakeMedianK(self, l: List[int], k: int) -> int:
        l.sort()
        co = 0
        med = len(l)//2 
        co+= abs(l[med]-k)
        for i in range(0,med):
            if l[i]>k:
                co+= abs(l[i]-k)
        for j in range(med+1, len(l)):
            if l[j]<k:
                co+=abs(l[j]-k)
        return co