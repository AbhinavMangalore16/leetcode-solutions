# Last updated: 3/31/2026, 9:32:59 PM
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (n+len(rolls))*mean
        missing = total-sum(rolls)
        if missing>6*n or missing<n:
            return []
        q,r = divmod(missing, n)
        return [q+1]*r+[q]*(n-r)