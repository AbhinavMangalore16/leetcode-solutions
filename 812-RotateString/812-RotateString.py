# Last updated: 3/31/2026, 9:36:47 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return False if len(s)!=len(goal) else (goal in s+s)