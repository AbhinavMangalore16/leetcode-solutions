# Last updated: 3/31/2026, 9:31:58 PM
class Solution:
    def countAsterisks(self, s: str) -> int:
        aster = 0
        e = 0
        for i in range(len(s)):
            if s[i]=="|" and e==0:
                e=1
            elif s[i]=="|" and e==1:
                e=0
            elif s[i]=="*" and e==0:
                aster+=1
        return aster