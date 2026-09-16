class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack question
        #O(n) time and O(n) space

        #Understand
        #input = list of ints representing temps
        #output = list of ints representing days after that day until a higher temp

        #Match - Stack Question

        #Plan

        n = len(temperatures)
        res = [0] * n
        stack = [] # will store indices: [i]

        for i, temp in enumerate(temperatures):
            #While current temp is warmer than the temp at the top of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            #Push current index onto the stack
            stack.append(i)
        
        return res