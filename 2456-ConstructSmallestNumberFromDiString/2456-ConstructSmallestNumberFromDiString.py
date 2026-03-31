# Last updated: 3/31/2026, 9:31:46 PM
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans, temp = ["1"], []
        for i, ch in enumerate(pattern):
            if ch == 'I':
                ans += temp[::-1] + [str(i + 2)]
                temp = []
            else:
                temp.append(ans.pop())
                ans.append(str(i + 2))
        return "".join(ans + temp[::-1])