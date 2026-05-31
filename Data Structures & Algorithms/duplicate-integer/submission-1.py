class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        so_far = set()
        for num in nums:
            if num in so_far:
                return True
            so_far.add(num)
        return False