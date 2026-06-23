class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k < 1:
            return None
        
        unique_num = len(set(nums))
        if k == unique_num:
            return list(set(nums))
        
        unique_dict = {}
        for n in nums:
            if n not in unique_dict:
                unique_dict[n] = 1
            else:
                unique_dict[n] += 1
        
        sorted_value_dict = dict(sorted(unique_dict.items(), key=lambda item: item[1]))
        keys = list(sorted_value_dict.keys())[-k:]
        
        return keys
            
        
        