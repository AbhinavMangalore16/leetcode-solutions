# Last updated: 3/31/2026, 9:33:56 PM
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        L = len(code)
        ans = [0]*L
        if not k:
            return ans
        for i in range(L):
            if k>0:
                for a in range(i+1, i+k+1):
                    ans[i] += code[a%L]
            else:
                for a in range(i+k, i):
                    ans[i] += code[(a+L)%L]
        return ans