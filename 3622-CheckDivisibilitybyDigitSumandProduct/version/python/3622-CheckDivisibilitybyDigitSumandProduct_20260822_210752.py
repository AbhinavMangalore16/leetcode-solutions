# Last updated: 8/22/2026, 9:07:52 PM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        R,C = n,10
4        rm = defaultdict(set)
5        for row,seat in reservedSeats:
6            if 1<seat<10:
7                rm[row].add(seat)
8        cin = [0,0,0]
9        grp = (n-len(rm))*2
10        for res in rm.values():
11            cin[0] = not(2 in res or 3 in res or 4 in res or 5 in res)
12            cin[1] = not(4 in res or 5 in res or 6 in res or 7 in res)
13            cin[2] = not(6 in res or 7 in res or 8 in res or 9 in res)
14            if cin[0] and cin[2]:
15                grp+=2
16            elif cin[0] or cin[1] or cin[2]:
17                grp+=1
18            cin[0]=cin[1]=cin[2]=0
19        return grp
20
21