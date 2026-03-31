# Last updated: 3/31/2026, 9:34:36 PM
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def build_lps(pattern: str) -> List[int]:
            lps= [0]*len(pattern)
            length = 0
            i = 1
            while i<len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        def kmp_search(text: str, pattern: str) -> bool:
            lps = build_lps(pattern)
            i = 0  
            j = 0  
            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                if j == len(pattern):
                    return True  
                elif i < len(text) and text[i] != pattern[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False
        
        result = set()
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and kmp_search(word2, word1):
                    result.add(word1)
        
        return list(result)