# Last updated: 3/31/2026, 9:34:35 PM
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD= 1000000007
        x,y= 6,6
        for i in range(2,n+1):
            X=(3*x+2*y)%MOD
            Y=(2*x+2*y)%MOD
            x,y=X,Y
        return (x+y)%MOD