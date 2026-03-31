# Last updated: 3/31/2026, 9:37:04 PM
class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        n = len(temperature)
        stack = []
        res = [0]*n
        ind = 0
        while ind < n:
            if not stack:
                stack.append((temperature[ind], ind))
            if temperature[ind]>stack[-1][0]:
                while stack and temperature[ind]>stack[-1][0]:
                    temp, i = stack.pop()
                    res[i] = ind - i
            stack.append((temperature[ind], ind))
            ind+=1
        return res