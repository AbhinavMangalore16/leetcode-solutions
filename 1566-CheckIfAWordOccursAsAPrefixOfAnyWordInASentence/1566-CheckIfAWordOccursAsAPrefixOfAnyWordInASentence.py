# Last updated: 3/31/2026, 9:34:30 PM
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i+1
        return -1