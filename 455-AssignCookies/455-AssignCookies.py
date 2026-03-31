# Last updated: 3/31/2026, 9:37:49 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookies = 0
        gp, sp = 0,0 
        while gp<len(g) and sp<len(s):
            if s[sp]>=g[gp]:
                cookies+=1
                gp+=1
            sp+=1
        return cookies
