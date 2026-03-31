# Last updated: 3/31/2026, 9:32:37 PM
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if (num==0 or num%10 !=0):
            return True
        else:
            return False