class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, combo):
            if target == 0:
                result.append(combo.copy())
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i, target - nums[i], combo)
                combo.pop()

        backtrack(0, target, [])
        return result