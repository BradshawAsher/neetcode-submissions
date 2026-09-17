import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search alg
        #length <= 10k = 10^4

        #understand
        #input = list of ints, where each number is the # of bananas in the ith pile
        #each hour, i can choose a pile of bananas and eat k bananas from that pile
        #cannot eat from another pile in the same hour, so i would assume that you can just start from the 0th index and go up since it really doesn't matter?

        #output = int = k, min int k so i can eat all bananas within h hours

        #so do we just guess binary search from 1 -> h and see if it works?

        #m - match = binary search

        #Plan - binary search
        #left = 0
        #right = 9

        #mid = 4
        #lowest_val = 4

        #simulate it? -> #pile0 gone, h =1
        #then, pile1 gone, h = 2, 
        #then pile 3 gone, h = 3
        #then pile 4 gone, h = 4

        #4 , 9, so right = 3
        #mid = 1
        #pile0 gone, h = 1
        #pile1 takes 4 hrs, h =5
        #pile2 takes 3 hrs, h = 8
        #pile 3 takes 2 hrs, h = 10
        #left = 2
        #mid = 2
        #pile1 gone,  h =1
        #pile 2 gone, h = 3
        #pile 3 gone, h = 5,
        #pile4 gone, h = 6

        #lowest_k = 2
        #return 2

        #O(nlogm) time and O(1) space, where n = input size, m = max value, 
        #lowest k starts at max(piles)

        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid_k = (left + right) // 2

            #ceiling division for each pile
            total_hours = sum(math.ceil(pile / mid_k) for pile in piles)

            if total_hours <= h:
                #valid speed: record answer and search left for a smaller viable speed
                ans = mid_k
                right = mid_k - 1
            
            else:
                #took too long: speed must be faster
                left = mid_k + 1
        return ans








