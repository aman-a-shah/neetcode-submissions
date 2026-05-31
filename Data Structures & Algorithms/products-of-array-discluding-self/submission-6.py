class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = [1] * len(nums)

        left_prod = 1
        for i, num in enumerate(nums):
            acc[i] *= left_prod
            left_prod*=num

        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            acc[i] *= right_prod
            right_prod*=nums[i]

        return acc