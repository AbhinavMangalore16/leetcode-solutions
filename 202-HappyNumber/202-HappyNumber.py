# Last updated: 3/31/2026, 9:38:59 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []
        while(n>0):
            s = 0
            while(n>0):
                dig = n%10
                s+=dig**2
                n = n//10
            if s in numbers:
                return False
            else:
                numbers.append(s)
            if (s==1):
                return True
            n = s
        return False

            