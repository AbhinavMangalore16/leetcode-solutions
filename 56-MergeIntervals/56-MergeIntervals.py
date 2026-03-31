# Last updated: 3/31/2026, 9:40:34 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        new = []
        for i in range(n):
            if not new or intervals[i][0] > new[-1][1]:
                new.append(intervals[i])
            else:
                new[-1][1] = max(new[-1][1],intervals[i][1])
        return new