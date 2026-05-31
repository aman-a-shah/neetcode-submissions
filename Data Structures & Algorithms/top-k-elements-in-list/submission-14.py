class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        acc = {}
        
        for num in nums:
            acc[num] = acc.get(num, 0) + 1
        
        # Sort numbers by their frequency (value) in descending order
        result = sorted(acc.keys(), key=lambda x: acc[x], reverse=True)
        return result[:k]