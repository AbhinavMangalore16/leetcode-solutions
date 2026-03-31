# Last updated: 3/31/2026, 9:37:18 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        minn, maxx = 0,0
        for i in range(len(s)):
            if s[i] == '(':
                minn +=1
                maxx +=1
            elif s[i] == ')':
                minn = max(0, minn-1)
                maxx -=1
            else:
                minn = max(0, minn-1)
                maxx+=1
            if maxx <0:
                return False
        if not minn:
            return True
        else:
            return False
            