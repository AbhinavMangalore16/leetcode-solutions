# Last updated: 3/31/2026, 9:33:37 PM
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        temp=[]
        for a,b in classes:
            ratio=(a-b)/((b)*(b+1))
            heapq.heappush(temp,[ratio,a,b])
        while extraStudents>0:
            ratio,a,b=heapq.heappop(temp)
            a=a+1
            b=b+1
            extraStudents-=1
            ratio=(a-b)/((b)*(b+1))
            heapq.heappush(temp,[ratio,a,b])
        ans=0.0
        while temp:
            _,a,b=heapq.heappop(temp)
            ans+=a/b
        return ans/len(classes)