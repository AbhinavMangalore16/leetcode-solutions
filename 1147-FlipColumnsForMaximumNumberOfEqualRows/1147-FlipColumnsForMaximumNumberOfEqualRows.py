# Last updated: 3/31/2026, 9:35:43 PM
class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        pat_freq = Counter()
        
        for r in mat:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r)
            pat_freq[pattern] += 1
            
        return max(pat_freq.values())