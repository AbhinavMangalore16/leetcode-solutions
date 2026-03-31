# Last updated: 3/31/2026, 9:29:15 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for i in s:
            if i.isdigit():
                stk.pop()
            else:
                stk.append(i)
        return "".join(stk)