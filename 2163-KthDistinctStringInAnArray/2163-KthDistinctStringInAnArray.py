# Last updated: 3/31/2026, 9:32:57 PM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in arr:
            if d[i] == 1:
                k-=1
            if k==0:
                return i
        return ""
            