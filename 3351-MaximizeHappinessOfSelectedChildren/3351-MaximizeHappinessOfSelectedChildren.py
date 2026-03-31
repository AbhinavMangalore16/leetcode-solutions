# Last updated: 3/31/2026, 9:29:31 PM
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        mirth = 0 
        for c in range(k):
            curr = happiness[c] - c
            if curr<=0:
                break
            mirth+=curr
        return mirth