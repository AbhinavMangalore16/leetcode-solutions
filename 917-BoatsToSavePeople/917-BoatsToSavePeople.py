# Last updated: 3/31/2026, 9:36:21 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        boats = 0
        while people[l]==limit:
            boats+=1
            l+=1
        while(l<r):
            if (people[l]+people[r]<=limit):
                boats+=1
                l+=1
                r-=1
            else:
                boats+=1
                l+=1
        if(l==r):
            boats+=1

        return boats