# Last updated: 3/31/2026, 9:33:23 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2:
                return num[:i+1]
        return ""