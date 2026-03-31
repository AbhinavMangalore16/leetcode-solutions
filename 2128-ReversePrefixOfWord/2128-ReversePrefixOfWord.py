# Last updated: 3/31/2026, 9:33:06 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st = ""
        i = 0
        while i < len(word) and word[i] != ch:
            st = word[i] + st
            i += 1
        if i < len(word):
            st = ch + st
        else:
            return word
        return st + word[i+1:]
        