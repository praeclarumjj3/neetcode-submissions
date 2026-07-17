class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for c in s:
            if c == "(":
                low += 1
                high += 1

            elif c == ")":
                low -= 1
                high -= 1

            else:  # "*"
                # "*" can act as ")" for the minimum
                # or "(" for the maximum
                low -= 1
                high += 1

            # Even with every previous "*" treated as "(",
            # we still have too many closing parentheses.
            if high < 0:
                return False

            # Unmatched opening count cannot be negative.
            low = max(low, 0)

        return low == 0