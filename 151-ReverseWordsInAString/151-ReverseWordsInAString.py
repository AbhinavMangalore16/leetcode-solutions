# Last updated: 3/31/2026, 9:39:25 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])