# Last updated: 3/31/2026, 9:34:28 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        curr = 0
        for i in range(0,k):
            if s[i] in vowels:
                curr+=1
        maxx = curr
        for i in range(k,len(s)):
            if s[i] in vowels:
                curr+=1
            if s[i-k] in vowels:
                curr-=1
            maxx = max(maxx,curr)
        return maxx