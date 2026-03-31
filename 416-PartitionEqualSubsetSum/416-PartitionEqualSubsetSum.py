# Last updated: 3/31/2026, 9:38:01 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        tgt = total //2
        n = len(nums)
        dp = [[False]*(tgt+1) for i in range(n+1)]
        for j in range(n+1):
            dp[j][0] = True
        for i in range(1,n+1):
            for j in range(1, tgt+1):
                if j<nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
        return dp[n][tgt]
        
