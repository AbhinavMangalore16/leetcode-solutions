# Last updated: 3/31/2026, 9:35:53 PM
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = float('inf')
        for val in range(1, 7):
            top_swaps = bottom_swaps = 0
            valid = True
            for t, b in zip(tops, bottoms):
                if t != val and b != val:
                    valid = False
                    break
                if t != val:
                    top_swaps += 1
                if b != val:
                    bottom_swaps += 1
            if valid:
                res = min(res, top_swaps, bottom_swaps)
        return -1 if res == float('inf') else res