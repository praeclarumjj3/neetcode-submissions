class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0

        heights.append(0)  # flush remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area