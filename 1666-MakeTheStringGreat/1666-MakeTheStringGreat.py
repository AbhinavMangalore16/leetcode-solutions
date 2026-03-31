# Last updated: 3/31/2026, 9:34:11 PM
class Solution:
    def makeGood(self, s: str) -> str:
        good = []
        for i in range(len(s)):
            if good and abs(ord(s[i]) - ord(good[-1])) == 32:
                good.pop()
            else:
                good.append(s[i])
        return ''.join(good)