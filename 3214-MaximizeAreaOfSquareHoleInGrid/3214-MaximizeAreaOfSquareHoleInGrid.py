# Last updated: 3/31/2026, 9:29:58 PM
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest(a):
            a.sort()
            best = cur = 1
            for i in range(1, len(a)):
                if a[i] == a[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best + 1

        side = min(longest(hBars), longest(vBars))
        return side * side