class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for start in range(n):
            tank = 0
            completed = True

            for steps in range(n):
                idx = (start + steps) % n
                tank += gas[idx]
                tank -= cost[idx]

                if tank < 0:
                    completed = False
                    break

            if completed:
                return start

        return -1