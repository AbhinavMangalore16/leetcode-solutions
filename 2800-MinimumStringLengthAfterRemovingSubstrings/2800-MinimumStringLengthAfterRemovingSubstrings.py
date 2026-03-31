# Last updated: 3/31/2026, 9:30:31 PM
class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if not stk:
                stk.append(c)
                continue
            if (c=="B" and stk[-1]=="A") or (c == "D" and stk[-1] == "C"):
                stk.pop()
            else:
                stk.append(c)
        return len(stk)