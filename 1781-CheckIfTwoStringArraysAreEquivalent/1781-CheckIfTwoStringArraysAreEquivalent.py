# Last updated: 3/31/2026, 9:33:52 PM
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = s2 = ""
        for i in range(len(word1)):
            s1 += word1[i]
        for i in range(len(word2)):
            s2 += word2[i]
        return s1==s2
