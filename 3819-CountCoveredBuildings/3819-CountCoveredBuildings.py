# Last updated: 3/31/2026, 9:28:33 PM
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cover = 0
        extrleft = [10**9]*(n+1)
        extright = [-1]*(n+1)
        extrdown = [-1]*(n+1)
        extrup = [10**9]*(n+1)
        for i, j in buildings:
            extrleft[i] = min(extrleft[i], j)
            extright[i] = max(extright[i],j)
            extrup[j] = min(extrup[j], i)
            extrdown[j] = max(extrdown[j], i)
        for i,j in buildings:
            if extrleft[i]<j<extright[i] and extrup[j]<i<extrdown[j]:
                cover+=1
        return cover