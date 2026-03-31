# Last updated: 3/31/2026, 9:40:32 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in s.rstrip():
            if i==" ":
                c=0
            else:
                c+=1
        return c