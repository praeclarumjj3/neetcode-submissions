class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _get_char_dict(string):
            count = {}
            for x in string:
                if x not in count:
                    count[x] = 1
                else:
                    count[x] += 1
            return count
        
        def _is_Anagram(str_1, str_2):
            if len(str_1) != len(str_2):
                return False
            count_1 = _get_char_dict(str_1)
            count_2 = _get_char_dict(str_2)

            for char in count_1:
                if char not in count_2:
                    return False
                elif count_1[char] != count_2[char]:
                    return False
            
            return True
        
        n = len(strs)
        if n == 1:
            return [strs]
        
        list_anagrams = []
        anagram_grp_idxs = {}
        idxs_covered = []

        for idx in range(n):
            if idx in idxs_covered:
                continue
            src_str = strs[idx]
            anagram_grp_idxs[idx] = []
            idxs_covered.append(idx)
            for j_idx in range(n-1-idx):
                is_anag = _is_Anagram(src_str, strs[j_idx+idx+1])
                if is_anag:
                    anagram_grp_idxs[idx].append(j_idx+idx+1)
                    idxs_covered.append(j_idx+idx+1)
        
        for ana_idx in anagram_grp_idxs:
            anags = []
            if len(anagram_grp_idxs[ana_idx]) > 0:
                anags.extend([strs[i] for i in anagram_grp_idxs[ana_idx]])
            
            anags.append(strs[ana_idx])

            if len(anags) > 0:
                list_anagrams.append(anags)
        return list_anagrams




        