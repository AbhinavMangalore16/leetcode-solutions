# Last updated: 3/31/2026, 9:35:19 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = []
        for i in range(len(s)):
            l.append(abs(ord(s[i]) - ord(t[i])))
        fp = 0
        sp = 0 
        temp = 0
        maxx = 0
        while (sp<len(s)):
            temp = temp + l[sp]
            sp+=1
            while (temp>maxCost):
                temp = temp - l[fp]
                fp+=1
            maxx = max(maxx, sp-fp)
        return maxx