# Last updated: 3/31/2026, 9:37:02 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for j in range(len(cost)-3,-1,-1):
            cost[j] = min(cost[j]+cost[j+1], cost[j]+cost[j+2])
        return min(cost[0], cost[1])
