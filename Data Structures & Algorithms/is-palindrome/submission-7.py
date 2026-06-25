class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        idx = 0
        st = []
        for c in s:
            if c.isalnum():
                st.append(c.lower())
        s = "".join(st)
        len_s = len(s)
        print(s)
        while idx < int(len_s/2):
            if s[idx] != s[len_s - idx - 1]:
                return False
            idx+=1
        
        return True
        