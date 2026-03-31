# Last updated: 3/31/2026, 9:30:48 PM
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = [0]*(n+1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            pre[i+1] = pre[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i+1] +=1
        res = []
        for q in queries:
            res.append(pre[q[1]+1] - pre[q[0]])
        return res
        