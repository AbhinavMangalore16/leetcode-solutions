# Last updated: 3/31/2026, 9:35:42 PM
class Solution:
    def buildChar(self, charCount):
        totalCount = 0
        for i in range(26):
            if charCount[i]:
                totalCount += 1
                charCount[i] -= 1
                totalCount += self.buildChar(charCount)
                charCount[i] += 1
        return totalCount

    def numTilePossibilities(self, tiles: str) -> int:
        charCount = [0] * 26
        for ch in tiles:
            charCount[ord(ch) - ord('A')] += 1
        return self.buildChar(charCount)
        