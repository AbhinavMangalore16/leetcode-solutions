# Last updated: 3/31/2026, 9:40:40 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for i in strs:
            c = [0]*26
            for j in i:
                c[ord(j) - ord('a')] +=1
            dic[tuple(c)].append(i)
        return dic.values()