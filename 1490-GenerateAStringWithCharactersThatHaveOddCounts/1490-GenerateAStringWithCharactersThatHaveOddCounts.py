# Last updated: 3/31/2026, 9:34:43 PM
class Solution:
    def generateTheString(self, n: int) -> str:
        s = ""
        for i in range(n-1):
            s+="a"
        if (n%2==0):
            s+="b"
            return s
        s+="a"
        return s