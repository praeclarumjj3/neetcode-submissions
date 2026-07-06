class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = nums[mid]
            print(mid, mid_value)
            if target > mid_value:
                low = mid + 1
            elif target < mid_value:
                high = mid - 1
            else:
                return mid
        return -1