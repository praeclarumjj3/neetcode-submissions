class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tgt_idx = None
        return_src_idx = None
        for src_idx in range(len(nums)):
            print("src_idx", src_idx)
            if tgt_idx is not None and return_src_idx is not None:
                break
            src = nums[src_idx]
            rem = target - src
            print("src, rem", src, rem)
            for j_idx in range(len(nums[src_idx+1:])):
                print("j_idx", j_idx)
                if rem == nums[src_idx+j_idx+1]:
                    tgt_idx = src_idx+j_idx+1
                    return_src_idx = src_idx
                    print("tgt_idx, return_src_idx", tgt_idx, return_src_idx)
                    break
                    
        return [return_src_idx, tgt_idx]
        