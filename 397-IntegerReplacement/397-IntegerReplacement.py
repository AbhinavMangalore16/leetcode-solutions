# Last updated: 3/31/2026, 9:38:06 PM
class Solution:
    def recur(self,n:int,dic) -> int:
        
        if (n==1):
            return 0
        if n in dic:
            return dic[n]
        if n%2==0:
            dic[n] = 1+self.recur(n//2,dic)
        else:
            dic[n] = 1+min(self.recur(n+1,dic), self.recur(n-1,dic))
        return dic[n]
    def integerReplacement(self, n: int) -> int:
        dic={}
        return self.recur(n,dic)