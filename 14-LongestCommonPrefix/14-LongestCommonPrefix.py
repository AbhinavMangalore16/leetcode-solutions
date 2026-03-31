# Last updated: 3/31/2026, 9:41:13 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        m = len(strs[0])
        for i in strs:
            m = min(m, len(i))
        for j in range(m):
            f = 1
            for k in range(1, len(strs)):
                if strs[k][j] != strs[0][j]:
                    f = 0
                    break
            if f:
                s += strs[0][j]
            else:
                break
        return s