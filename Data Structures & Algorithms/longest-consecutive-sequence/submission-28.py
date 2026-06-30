class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        nums = sorted(nums)
        
        n = nums[0]

        subseq = {
            n: [1]
        }
        max_n = 1


        for idx in range(1, len(nums)):
            n = nums[idx]
            
            if n-1 in subseq.keys():
                subseq[n] = [i+1 for i in subseq[n-1]]
            else:
                subseq[n] = [1]
            max_n = max(max_n, max(subseq[n]))
            print(max_n)

        print(subseq)
        return max_n
            
                
        