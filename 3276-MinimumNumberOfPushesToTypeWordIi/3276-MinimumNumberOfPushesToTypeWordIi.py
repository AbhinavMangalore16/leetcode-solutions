# Last updated: 3/31/2026, 9:29:45 PM
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(f*(i//8+1) for i, f in enumerate(sorted(Counter(word).values(), reverse=True)))
        