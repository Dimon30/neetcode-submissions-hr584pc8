class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0

        for pos, sp in cars:
            cur_time = (target - pos) / sp
            if cur_time > last_time:
                fleets += 1
                last_time = cur_time

        return fleets