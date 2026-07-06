class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time_ahead = 0

        for p, s in cars:
            time = (target - p) / s

            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time

        return fleets