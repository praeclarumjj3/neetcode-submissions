class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        num_dict = {}

        for idx, n in enumerate(nums):
            if n in num_dict:
                num_dict[n].append(idx)
            else:
                num_dict[n] = [idx]
        
        key_set = list(num_dict.keys())

        if len(key_set) == 1 and key_set[0] == 0:
            return [[0, 0, 0]]

        triplets = []
        print(key_set)
        two_sum_list = {}
        for idx, k in enumerate(key_set):
            for j in key_set[idx:]:
                if k == j and len(num_dict[j]) == 1:
                    continue
                key = -(k + j)
                if key in num_dict.keys():
                    key_idx = num_dict[key]
                    j_idx = num_dict[j]
                    k_idx = num_dict[k]

                    if len(key_idx) == 1 and ((key == k) or (key == j)):
                        continue
                    
                    idxs = key_idx + j_idx + k_idx
                    num_unique_idxs = len(set(idxs))
                    if num_unique_idxs >=3:
                        triplet = sorted([key, k, j])
                        print(idxs, num_unique_idxs, triplet, [key, k, j])
                        if triplet not in triplets:
                            triplets.append(triplet)
        
        return triplets


        