# Last updated: 3/31/2026, 9:29:36 PM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse = True)
        B = 0
        for i in capacity:
                B+=1
                apples -= i
                if apples<=0:
                    break
        return B
