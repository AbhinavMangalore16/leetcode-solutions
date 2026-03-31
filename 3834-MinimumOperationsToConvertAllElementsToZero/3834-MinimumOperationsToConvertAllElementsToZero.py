# Last updated: 3/31/2026, 9:28:31 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk=[-1]
        op=0
        for x in nums:
            while x<stk[-1]: 
                stk.pop()
            if x>stk[-1]:
                op += (x>0) 
                stk.append(x)
        return op