class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        digits = digits[::-1]

        for i in range(len(digits)):
            s = digits[i] + carry
            num = (s) % 10
            carry = s // 10
            digits[i] = num
        
        if carry:
            digits.append(carry)
        
        return digits[::-1]