# Last updated: 3/31/2026, 9:33:13 PM
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R = len(points)
        C = len(points[0])
        row = points[0]
        for r in range(1, R):
            next_row = points[r].copy()
            left, right = [0]*C, [0]*C
            left[0] = row[0]
            for c in range(1, C):
                left[c] = max(left[c-1]-1, row[c])
            right[-1] = row[-1]
            for c in range(C-2, -1,-1):
                right[c] = max(right[c+1]-1, row[c])
            for c in range(C):
                next_row[c] += max(left[c], right[c])
            row = next_row
        return max(row)