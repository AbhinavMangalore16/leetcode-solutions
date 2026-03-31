# Last updated: 3/31/2026, 9:35:34 PM
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_map = defaultdict(int)
        count = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count += count_map[key]
            count_map[key] += 1

        return count