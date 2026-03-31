# Last updated: 3/31/2026, 9:31:00 PM
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        go = 1
        d = 1
        while time:
            go += d
            if go==n:
                d=-1
            elif go==1:
                d=1
            time-=1
        return go