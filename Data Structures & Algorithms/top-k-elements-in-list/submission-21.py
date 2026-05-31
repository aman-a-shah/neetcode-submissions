class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        acc = {}

        for num in nums:
            if num in acc:
                acc[num] += 1
            else:
                acc[num] = 1

        result = sorted(acc.keys(), key=lambda x: acc[x], reverse=True)
        return result[:k]