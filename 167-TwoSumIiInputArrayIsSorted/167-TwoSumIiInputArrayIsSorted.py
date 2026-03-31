# Last updated: 3/31/2026, 9:39:17 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        l = []
        while (low<high):
            s = numbers[low] + numbers[high]
            if (s>target):
                high-=1
            elif (s<target):
                low+=1
            else:
                l.append(low+1)
                l.append(high+1)
                return l