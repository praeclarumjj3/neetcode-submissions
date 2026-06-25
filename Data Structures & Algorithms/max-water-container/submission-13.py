class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if len(heights) == 2:
            return min(heights)
        
        left = 0
        right = 1

        max_area = 0
        while right < len(heights):
            left = 0
            while left < right:
                # print(left, right)
                area = (min(heights[left], heights[right]) * abs(right-left))

                max_area = max(max_area, area)

                left += 1
            
            right += 1
        
        return max_area



        