class TimeMap:

    def __init__(self):
        self.time = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.time:
            self.time[key] = {
                "moods": [value],
                "time": [timestamp]
            }
        else:
            self.time[key]["moods"].append(value)
            self.time[key]["time"].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        
        times = self.time[key]["time"]
        if len(times) == 0:
            return ""
        
        low = 0
        high = len(times) - 1

        if times[low] > timestamp:
            return ""
        elif times[high] < timestamp:
            return self.time[key]["moods"][high]

        while low < high:
            mid = (low + high) // 2
            mid_value = times[mid]
            
            if mid_value == timestamp:
                return  self.time[key]["moods"][mid]
            
            if mid_value > timestamp:
                high = mid - 1
            else:
                low = mid + 1
                if times[low] > timestamp:
                    return self.time[key]["moods"][low-1]
        
        return self.time[key]["moods"][low]


        
