from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        idx = bisect_left(self.arr, num)
        self.arr = self.arr[:idx] + [num] + self.arr[idx:]
        

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            return self.arr[(len(self.arr)-1)//2]
        else:
            return (self.arr[(len(self.arr)-1)//2] + self.arr[(len(self.arr))//2]) / 2
        
        