# Last updated: 3/31/2026, 9:35:04 PM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t=0
        for p in range(len(points)-1):
            dx = abs(points[p][0]-points[p+1][0])
            dy = abs(points[p][1]-points[p+1][1])
            t+= max(dx,dy)
        return t