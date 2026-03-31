# Last updated: 3/31/2026, 9:29:08 PM
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        groups = 0
        alt_count = 0 
        for a, b in pairwise(chain(colors, colors[:k])): 
            alt_count = alt_count + 1 if a != b else 1 
            groups += 1 if alt_count >= k else 0 

        return groups