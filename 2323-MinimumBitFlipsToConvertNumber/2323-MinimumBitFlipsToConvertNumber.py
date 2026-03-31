# Last updated: 3/31/2026, 9:32:09 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        count = 0
        while xor_result > 0:
            count += xor_result & 1  
            xor_result >>= 1         
        
        return count