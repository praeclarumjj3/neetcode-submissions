class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def _get_count_alphabets(str_seq):
            s_conts = {}
            for x in str_seq:
                if x not in s_conts:
                    s_conts[x] = 1
                else:
                    s_conts[x] += 1
            return s_conts
        
        if len(s) != len(t):
            return False
        
        s_conts = _get_count_alphabets(s)
        t_conts = _get_count_alphabets(t)

        for k in s_conts:
            if k in t_conts and t_conts[k] != s_conts[k]:
                return False
            elif k not in t_conts:
                return False
        return True
        