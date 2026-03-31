# Last updated: 3/31/2026, 9:33:05 PM
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n != len(original)):
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]