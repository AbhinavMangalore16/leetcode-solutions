# Last updated: 3/31/2026, 9:35:36 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict 
        cm = defaultdict(int)
        rem = []
        res = []
        for i in arr2:
            cm[i] = 0
        for n in arr1:
            if n in cm:
                cm[n] +=1
            else:
                rem.append(n)
        rem.sort()
        for j in arr2:
            res.extend([j]*cm[j])
        res.extend(rem)
        return res