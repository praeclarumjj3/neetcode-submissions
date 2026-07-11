class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans <<= 1          # make room
            ans |= n & 1       # copy last bit
            n >>= 1            # remove last bit

        return ans