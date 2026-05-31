class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtrn_lst = []

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    rtrn_lst.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
 
                    left += 1
                    right -= 1

        return rtrn_lst