class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
        
        cur = 0
        max_len = 0
        sub_str = ""
        c = s[cur]

        while c not in sub_str:
            sub_str += c
            cur += 1
            if cur == len(s):
                break
            c = s[cur]
        
        if cur < len(s):
            for idx, p in enumerate(sub_str):
                if p == c:
                    break
            
            print(idx, p, cur, len(sub_str))
            
            new_idx = cur - len(sub_str) + idx + 1
            if new_idx >= len(s):
                return len(sub_str)
            
            max_len = max(len(sub_str), self.lengthOfLongestSubstring(s[new_idx:]))
        else:
            return len(sub_str)
        return max_len
        