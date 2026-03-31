# Last updated: 3/31/2026, 9:38:30 PM
class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        return 9 if not num%9 else num%9