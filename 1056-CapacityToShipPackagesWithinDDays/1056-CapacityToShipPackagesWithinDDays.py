# Last updated: 3/31/2026, 9:35:51 PM
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, u = max(weights), sum(weights)
        while l<u:
            midcap = (l+u)//2
            days, cont = 1,0
            for i in range(len(weights)):
                if cont + weights[i] > midcap:
                    days+=1
                    cont = 0
                cont = cont + weights[i]
            if days>D:
                l=midcap+1
            else:
                u = midcap
        return l