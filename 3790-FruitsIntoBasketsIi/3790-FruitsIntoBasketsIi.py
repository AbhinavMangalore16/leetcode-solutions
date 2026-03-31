# Last updated: 3/31/2026, 9:28:35 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n =len(fruits)
        assign = [0]*n
        unassigned = 0 
        for i in range(n):
            assigned = False
            for j in range(n):
                if not assign[j] and fruits[i] <=baskets[j]:
                    assign[j]=True
                    assigned = True 
                    break
            if not assigned:
                unassigned +=1
        return unassigned
