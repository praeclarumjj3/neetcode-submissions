class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0

        area = 0
        left = 0
        

        hl = 0
        hl = height[left]
        while height[left] >= hl:
            hl = height[left]
            left += 1
        
        left -= 1
        cur = left + 1
        
        right = len(height) - 1
        hr = 0

        while height[right] >= hr:
            hr = height[right]
            right -= 1
        
        right += 1
        # max_area = min(height[left], height[right]) * (right - left - 1)
        max_area = 0

        while cur < right:
            hl = height[left]
            hc = height[cur]

            if hc < hl:
                max_area += (hl - hc)
            else:
                left = cur
            
            cur += 1
            if cur == right and height[right] < height[left]:
                left = left + 1
                while left < right:
                    max_area = (
                        max_area - (hl - height[left]) + max(0, (height[right] - height[left]))
                    )
                    left += 1

        return max_area
        