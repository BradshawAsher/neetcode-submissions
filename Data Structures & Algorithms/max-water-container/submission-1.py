class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Understand
        #input = heights -> list of ints representing heights
        #the width is just representing by their indeces
        #output = int of the max amt of water a container can store

        #m - match -> 2 pointers, o(n) time, o(1) space

        #Plan
        #two pointers
        #probably one at the left, one at the right
        #the area is represented by the (smaller bar * width)
        #store the max value in a var and then yeah
        #always move the one with the greater delta like look for the difference in delta and always move to the one with the bigger increase in delta first?
        #always make the move that leads to a higher positive delta h

        max_area = 0
        left = 0
        right = len(heights)-1

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                #move the left right
                left += 1
            else:
                right -= 1
            
        return max_area
       








       