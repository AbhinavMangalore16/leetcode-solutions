# Last updated: 9/27/2026, 3:43:59 AM
1class Solution:
2    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
3        d = dict(knowledge)
4        ans, start = [], -1
5        for i, c in enumerate(s):
6            if c == "(":
7                start = i
8            elif c == ")":
9                ans.append(d.get(s[start + 1 : i], "?"))
10                start = -1
11            elif start < 0:
12                ans.append(c)
13        return "".join(ans)