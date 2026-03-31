# Last updated: 3/31/2026, 9:32:02 PM
import math
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = 100
        for i in target:
            ans = min(ans, s.count(i)//target.count(i))
        return ans