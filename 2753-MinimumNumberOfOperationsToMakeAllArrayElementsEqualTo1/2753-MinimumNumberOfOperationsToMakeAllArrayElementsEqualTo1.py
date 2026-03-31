# Last updated: 3/31/2026, 9:30:39 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c1 = 0
        N = len(nums)
        og = 0
        for i in range(N):
            if nums[i]==1:
                c1+=1
            og = gcd(og, nums[i])
        if og>1:
            return -1
        if c1:
            return N-c1
        minn = float('inf')
        for i in range(N):
            g = nums[i]
            for j in range(i+1, N):
                g = gcd(g, nums[j])
                if g==1:
                    minn = min(minn, j - i)
                    break
        if minn == float('inf'):
            return -1

        return (N - 1) + minn