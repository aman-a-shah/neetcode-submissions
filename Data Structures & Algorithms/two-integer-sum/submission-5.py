class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i in range(len(nums)):
            targets[target-nums[i]] = i;
        
        for j in range(len(nums)):
            if nums[j] in targets:
                if j != targets[nums[j]]:
                    return [j, targets[nums[j]]]