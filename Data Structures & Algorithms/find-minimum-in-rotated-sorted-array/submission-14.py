class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        is_rotated = nums[-1] < nums[0]

        if not is_rotated:
            return nums[0]

        while low <= high:
            mid = (low + high) // 2
            mid_value = nums[mid]

            print(mid, mid_value, nums[low], nums[high])

            if mid_value < nums[mid - 1]:
                return mid_value

            if mid_value == nums[low]:
                if nums[high] < nums[low]:
                    return nums[high]
            elif mid_value > nums[low] and mid_value > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
        
        return mid_value

