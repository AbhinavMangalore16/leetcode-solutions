# Last updated: 3/31/2026, 9:38:11 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f = {}
        res = []
        for i in nums1:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        for i in nums2:
            if i in f and f[i]>0:
                res.append(i)
                f[i]-=1
        return res