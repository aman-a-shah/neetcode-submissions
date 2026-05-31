class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        cur_longest = 0

        dif_nums = set(nums)

        for num in dif_nums:
            cur_longest = 1

            while num + 1 in dif_nums:
                cur_longest += 1
                num += 1
            
            longest = max(longest, cur_longest)

        return longest