# Last updated: 4/1/2026, 3:58:40 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        grp = {}
4        n = len(strs)
5        for i in range(n):
6            word = strs[i]
7            freq = [0]*26
8            for j in range(len(word)):
9                freq[ord(word[j])-97] +=1
10            k = tuple(freq)
11            if k not in grp:
12                grp[k] = []
13            grp[k].append(word)
14        return list(grp.values())