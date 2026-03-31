# Last updated: 3/31/2026, 9:36:45 PM
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        assigned = list(zip(difficulty,profit))
        mp = 0
        wb = 0
        assigned.sort()
        worker.sort()
        j=0
        for work in worker:
            while j<len(assigned) and work >=assigned[j][0]:
                wb = max(wb, assigned[j][1])
                j+=1
            mp+=wb
        return mp 
        