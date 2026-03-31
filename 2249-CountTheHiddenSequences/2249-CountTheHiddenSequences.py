# Last updated: 3/31/2026, 9:32:30 PM
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = y = cur = 0
        for d in differences:
            cur += d
            x = min(x, cur)
            y = max(y, cur)
            if y - x > upper - lower:
                return 0
        return (upper - lower) - (y - x) + 1