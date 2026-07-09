class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapq.heapify(arr)

        for n in nums:
            heapq.heappush(arr, n)
            if len(arr) > k:
                heapq.heappop(arr)
        
        
        return heapq.heappop(arr)