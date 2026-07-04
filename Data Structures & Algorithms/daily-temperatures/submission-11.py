class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            print(stack, t, idx)
            if len(stack) and t > stack[-1][0]:
                days[idx-1] = 1
                stack.pop()
                while len(stack) and t > stack[-1][0]:
                    tidx = stack.pop()[-1]
                    days[tidx] = idx - tidx              
            stack.append((t, idx))
        return days
                
        