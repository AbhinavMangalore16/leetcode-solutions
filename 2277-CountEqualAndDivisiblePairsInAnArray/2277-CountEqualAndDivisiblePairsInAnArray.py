# Last updated: 3/31/2026, 9:32:23 PM
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        mpp = defaultdict(list)
        for i in range(len(nums)):
            mpp[nums[i]].append(i)

        divisors = []
        for d in range(1, int(k**0.5) + 1):
            if k % d == 0:
                divisors.append(d)
                if d != k // d:
                    divisors.append(k // d)

        for vec in mpp.values():
            mpp2 = defaultdict(int)
            for i in vec:
                gcdd = gcd(i, k)
                need = k // gcdd
                pairs += mpp2[need]
                for d in divisors:
                    if i % d == 0:
                        mpp2[d] += 1

        return pairs