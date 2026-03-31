# Last updated: 3/31/2026, 9:40:33 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            merged = []
            i = 0
            n = len(intervals)
            
            # Add intervals that come before newInterval
            while i < n and intervals[i][1] < newInterval[0]:
                merged.append(intervals[i])
                i += 1
            
            # Merge overlapping intervals with newInterval
            while i < n and intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
            
            merged.append(newInterval)
            
            # Add remaining intervals
            while i < n:
                merged.append(intervals[i])
                i += 1
            
            return merged
        