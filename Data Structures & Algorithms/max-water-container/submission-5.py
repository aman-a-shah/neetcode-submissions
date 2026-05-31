class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            cur_area = min(heights[left], heights[right])*(right-left)
            max_area = max(max_area, cur_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

            # while left < right and heights[left+1] < heights[left]:
            #     left += 1
            # while left < right and heights[right-1] < heights[right]:
            #     right -= 1
            

        return max_area