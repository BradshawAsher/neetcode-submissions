class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Pair positions with speeds and sort in descending order of position
        pair = sorted(zip(position, speed), reverse = True)

        fleets = 0
        prev_time = 0.0

        for pos, spd in pair:
            time = (target - pos) / spd
            
            #If this car takes longer than the fleet ahead, it becomes a new fleet leader
            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets

