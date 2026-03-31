# Last updated: 3/31/2026, 9:38:13 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            freq_dic[i] = freq_dic.get(i,0) + 1
        for key,v in freq_dic.items():
            freq[v].append(key)
            
        elements = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                elements.append(j)
                if len(elements) == k:
                    return elements
        
        
        