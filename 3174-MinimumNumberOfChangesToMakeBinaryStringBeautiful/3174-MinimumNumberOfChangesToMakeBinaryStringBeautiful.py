# Last updated: 3/31/2026, 9:30:07 PM
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                count += 1
            i += 2
        return count