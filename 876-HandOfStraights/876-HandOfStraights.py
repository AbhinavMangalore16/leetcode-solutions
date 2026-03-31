# Last updated: 3/31/2026, 9:36:38 PM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize:
            return False
        d = {}
        for i in range(len(hand)):
            d[hand[i]] = d.get(hand[i], 0) + 1
        for j in sorted(d.keys()):
            if d[j]>0:
                need = d[j]
                for k in range(j, j+groupSize):
                    if d.get(k,0)<need:
                        return False
                    d[k]-=need
        return True