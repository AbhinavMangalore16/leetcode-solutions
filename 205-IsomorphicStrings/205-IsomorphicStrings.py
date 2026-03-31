# Last updated: 3/31/2026, 9:39:04 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hS = [0]*200
        hT = [0]*200
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if hS[ord(s[i])] != hT[ord(t[i])]:
                return False
            hS[ord(s[i])] = i+1
            hT[ord(t[i])] = i+1
        return True
        