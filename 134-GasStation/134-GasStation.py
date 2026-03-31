# Last updated: 3/31/2026, 9:39:47 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas)<sum(cost)):
            return -1
        fuel = 0
        ind = 0
        for i in range(len(gas)):
            f = gas[i] - cost[i]
            fuel+= f
            if fuel<0:
                ind = i+1
                fuel = 0
        return ind