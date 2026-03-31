# Last updated: 3/31/2026, 9:32:40 PM
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        T, res = 1, 0
        triangle = lambda x: x * (x + 1)//2
        for p1, p2 in pairwise(prices):
            if p1 - p2 == 1:
                T+= 1
            else:
                res+= triangle(T)
                T = 1    
        res+= triangle(T)
        return  res