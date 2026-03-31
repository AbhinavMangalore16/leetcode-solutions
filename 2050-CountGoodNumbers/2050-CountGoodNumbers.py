# Last updated: 3/31/2026, 9:33:18 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n + 1) // 2
        odd = n // 2
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod