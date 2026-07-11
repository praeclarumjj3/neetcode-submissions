class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        num_1s = 0
        for i in b:
            if i == "1":
                num_1s += 1
        return num_1s
        