# Last updated: 3/31/2026, 9:30:51 PM
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        
        total_count = count1 + count2
        for fruit, count in total_count.items():
            if count % 2 != 0:
                return -1  
        surplus1 = []
        surplus2 = []
        for fruit in total_count:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                surplus1.extend([fruit] * (diff // 2))
            elif diff < 0:
                surplus2.extend([fruit] * (-diff // 2))
        
        surplus1.sort()
        surplus2.sort(reverse=True)
        
        min_elem = min(min(basket1), min(basket2))
        total_cost = 0
        
        for a, b in zip(surplus1, surplus2):
            total_cost += min(min(a, b), 2 * min_elem)
        
        return total_cost