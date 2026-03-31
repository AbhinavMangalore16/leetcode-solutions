# Last updated: 3/31/2026, 9:33:50 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedstr = set(allowed)
        cons = 0
        for word in words:
            if all(ch in allowedstr for ch in word):
                cons+=1
        return cons