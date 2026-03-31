# Last updated: 3/31/2026, 9:32:38 PM
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = back = 0
        for s in bank:
            r = s.count('1')
            if r:
                lasers += r*back
                back = r
        return lasers        