class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in matrix:
            if r[0] > target:
                return False
            if r[0] <= target and r[-1] >= target:
                low = 0
                high = len(r) - 1
                while low <= high:
                    mid = (low + high) // 2
                    mid_val = r[mid]
                    if mid_val == target:
                        return True
                    elif mid_val > target:
                        high = mid - 1
                    else:
                        low = mid + 1

        
        return False