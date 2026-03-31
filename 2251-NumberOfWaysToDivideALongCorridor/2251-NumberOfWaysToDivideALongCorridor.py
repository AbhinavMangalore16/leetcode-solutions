# Last updated: 3/31/2026, 9:32:28 PM
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        ts = corridor.count('S')
        if ts == 0 or ts % 2 != 0:
            return 0
        ways,sc,pc = 1,0,0
        for c in corridor:
            if c == 'S':
                sc += 1
                if sc > 2 and sc % 2 == 1:
                    ways = (ways * (pc + 1)) % MOD
                    pc = 0
            else:
                if sc % 2 == 0 and sc > 0:
                    pc += 1
        return ways