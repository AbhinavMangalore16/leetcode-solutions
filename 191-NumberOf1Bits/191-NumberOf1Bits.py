# Last updated: 3/31/2026, 9:39:12 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n!=0):
            n = n & (n-1)
            count+=1
        return count