# Last updated: 3/31/2026, 9:30:36 PM
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix= [0] * n

        for curr in range(n):
            common_count = 0
            for a in range(curr + 1):
                for b in range(curr + 1):
                    if A[a] == B[b]:
                        common_count += 1
                        break
            prefix[curr] = common_count
        return prefix