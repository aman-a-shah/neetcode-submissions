class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # helper for bst
        def helper(lst, offset):
            if not lst:
                return -1

            mid = len(lst)//2

            if lst[mid] == target:
                return (mid+offset)%len(nums)
            elif lst[mid] < target:
                return helper(lst[mid+1:], offset+mid+1)
            elif lst[mid] > target:
                return helper(lst[:mid], offset)
        
        # find rotation amount
        rot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rot = i
        
        new_list = nums[rot:] + nums[:rot]
        return helper(new_list, rot)