class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Pair positions with speeds and sort in descending order of position
        pair = sorted(zip(position, speed), reverse = True)

        stack = [] #will store arrival times of fleet leaders

        for pos, spd in pair:
            time = (target - pos) / spd
            stack.append(time)

            #If the current car arrives faster than or at the same time as 
            #the fleet ahead of it, it caches up and merges to it (pop it)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

