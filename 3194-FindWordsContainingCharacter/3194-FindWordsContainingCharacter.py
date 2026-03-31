# Last updated: 3/31/2026, 9:30:02 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, w in enumerate(words):
            if w.count(x):
                res.append(i)
        return res