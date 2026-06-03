class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]

        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        
        return min_num