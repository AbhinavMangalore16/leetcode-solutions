# Last updated: 3/31/2026, 9:33:41 PM
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        
        return True