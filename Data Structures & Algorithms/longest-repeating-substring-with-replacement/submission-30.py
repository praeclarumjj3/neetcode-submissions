class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            window_len = right - left + 1

            while window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_len = right - left + 1

            ans = max(ans, window_len)

        return ans