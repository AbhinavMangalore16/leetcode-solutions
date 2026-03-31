# Last updated: 3/31/2026, 9:36:33 PM
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)  
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]

        dq = deque()  
        ans = n + 1  
        
        for i in range(n + 1):
            while dq and presum[i] - presum[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            while dq and presum[i] <= presum[dq[-1]]:
                dq.pop()
            dq.append(i)
        return ans if ans <= n else -1