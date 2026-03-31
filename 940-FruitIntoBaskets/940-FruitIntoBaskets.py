# Last updated: 3/31/2026, 9:36:16 PM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0,0
        basket = {}
        maxx = 0
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            while len(basket)>2:
                basket[fruits[l]] -=1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l+=1
            maxx = max(maxx, r-l+1)
        return maxx
