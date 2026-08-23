# Last updated: 8/23/2026, 11:57:13 PM
1class Solution:
2    def sumGame(self, num: str) -> bool:
3        N = len(num)
4        def help(st):
5            q,s = 0,0
6            for i in range(len(st)):
7                if st[i]=='?':
8                    q+=1
9                else:
10                    s+=int(st[i])
11            return s,q
12        sL,qL = help(num[:N//2])
13        sR,qR = help(num[N//2:])
14        if (qL+qR)%2:
15            return True
16        alice = ((sL-sR)!=(9*(qR-qL)//2))
17        return alice