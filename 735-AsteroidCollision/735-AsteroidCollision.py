# Last updated: 3/31/2026, 9:37:05 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1]>0 and a<0:
                if stk[-1]<-a:
                    stk.pop()
                    continue
                elif stk[-1]==-a:
                    stk.pop()
                break
            else:
                stk.append(a)
        return stk