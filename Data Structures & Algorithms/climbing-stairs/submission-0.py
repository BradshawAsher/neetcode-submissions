class Solution:
    def climbStairs(self, n: int) -> int:
        #start from beginning (low) to end (large)
        #what is the dp formula?
        if n <= 2:
            return n

        dp = [0] * (n+1)
        

        dp[1] = 1
        dp[2] = 2

        for cur in range(3, n+1):
            dp[cur] = dp[cur-1] + dp[cur-2]


        return dp[n]