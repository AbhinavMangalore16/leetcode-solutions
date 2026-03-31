# Last updated: 3/31/2026, 9:32:25 PM
class Solution:
    def minimumSum(self, num: int) -> int:
        app = []
        while num>0:
            app.append(num%10)
            num//=10
        app.sort()
        return (app[0]*10 + app[-1] + app[1]*10 + app[-2])