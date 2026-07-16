class Solution:
    def countSubstrings(self, s: str) -> int:
        num_substrings = 0
        
        for idx in range(len(s)):
            start = idx
            for end in range(idx, len(s)):
                while start <= end:
                    if s[start] != s[end]:
                        break
                    else:
                        start += 1
                        end -= 1
                
                if start >= end:
                    num_substrings += 1
                start = idx
        
        return num_substrings
        
                    

        