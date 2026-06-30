from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                # update answer
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # shrink from left
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        l, r = res
        return "" if res_len == float("inf") else s[l:r+1]