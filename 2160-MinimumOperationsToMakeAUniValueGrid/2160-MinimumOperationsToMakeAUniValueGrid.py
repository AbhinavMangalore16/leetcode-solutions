# Last updated: 3/31/2026, 9:32:58 PM
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = sorted([val for row in grid for val in row])
        
        diff = [abs(val - values[0]) % x for val in values]
        if any(d != 0 for d in diff):
            return -1
        
        median = values[len(values) // 2]
        operations = sum(abs(val - median) // x for val in values)
        
        return operations