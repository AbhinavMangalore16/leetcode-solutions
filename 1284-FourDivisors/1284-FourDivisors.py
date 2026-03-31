# Last updated: 3/31/2026, 9:35:27 PM
class Solution:
    def isPrime(self, x: int) -> bool:
        if (x<2):
            return False
        for i in range(2, int(x**0.5)+1):
            if not (x%i):
                return False
        return True
    def sumFourDivisors(self, nums: List[int]) -> int:
        summ = 0
        for i in nums:
            pm = int(round(i**(1/3)))
            if pm**3==i and self.isPrime(pm):
                summ+= (1+i+pm+pm*pm)
                continue
            for j in range(2,int(i**0.5)+1):
                if (i%j==0):
                    m = i//j
                    if j!=m and self.isPrime(j) and self.isPrime(m):
                        summ+= (1+i+j+m)
                    break
        return summ

        