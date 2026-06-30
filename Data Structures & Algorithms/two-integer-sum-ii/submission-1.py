class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx in range(len(numbers)-1):
            src = target - numbers[idx]
            if src in numbers[idx+1:]:
                low = idx+1
                high = len(numbers) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if numbers[low] == src:
                        return [idx+1, low+1]
                    elif numbers[high] == src:
                        return [idx+1, high+1]
                    elif numbers[mid] == src:
                        return [idx+1, mid+1]
                    elif numbers[mid] > src:
                        high = mid - 1
                    elif numbers[mid] < src:
                        low = mid + 1
        
                
        