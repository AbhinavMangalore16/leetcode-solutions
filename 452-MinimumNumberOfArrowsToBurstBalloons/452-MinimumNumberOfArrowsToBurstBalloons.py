# Last updated: 3/31/2026, 9:37:51 PM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # for i in range(len(points)):
        #     for j in range(len(points)-1):
        #         if points[j][1] > points[j+1][1]:
        #             temp = points[j]
        #             points[j] = points[j+1]
        #             points[j+1] = temp
        points.sort(key=lambda x: x[1])
        arrow = t = 0
        for i in range(1,len(points)):
            if points[i][0] > points[t][1]:
                arrow+=1
                t= i
        return arrow+1