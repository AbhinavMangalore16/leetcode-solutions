# Last updated: 3/31/2026, 9:35:47 PM
class Solution:
    def good(self, j: str, main: List[int]) -> bool:
        c = [0] * 26
        for w in j:
            el = ord(w) - ord('a')
            c[el] +=1
            if c[el] > main[el]:
                return False
        return True 

    def countCharacters(self, words: List[str], chars: str) -> int:
        main = [0]*26
        for i in chars:
            main[ord(i)-ord('a')] += 1
        goodsum = 0
        for j in words:
            if self.good(j, main):
                goodsum+=len(j)
        return goodsum


