class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #U - Understand
        #input = m and n, mxn grid
        #output, int for # of ways

        #M - match -> dp

        #P - Plan
        #So you can go down and to the right, and each thing is the sum of its upper and lefter (need to check bounds)
        if not m or not n:
            return 0

        rows, cols = m, n
        dp = [[0] * cols for _ in range(rows)]


        dp[0][0] = 1
        root = True

        #just go through every item in the grid
        for r in range(rows):
            for c in range(cols):
                #check bounds
                tile_ways = 0
                #check for upper parent
                if r != 0:
                    tile_ways += dp[r-1][c]
                
                #check for left parent
                if c != 0:
                    tile_ways += dp[r][c-1]

                if root:
                    root = False
                else:
                    dp[r][c] = tile_ways
        
        return dp[-1][-1]
        