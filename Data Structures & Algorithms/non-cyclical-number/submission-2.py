class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        def get_square_sum(n):
            dgs = []
            while n >= 10:
                d = n % 10
                dgs.append(d)
                n = n // 10
            dgs.append(n)
            return sum([d**2 for d in dgs])
        
        while n not in seen:
            seen.add(n)
            n = get_square_sum(n)
            if n == 1:
                return True
        
        return False