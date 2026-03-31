# Last updated: 3/31/2026, 9:33:24 PM
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        lang = len(part)
        match_end = part[-1]
        for i in s:
            stk.append(i)
            if match_end == i and lang<=len(stk):
                if "".join(stk[-lang:]) == part:
                    del stk[-lang:]
        return "".join(stk)
