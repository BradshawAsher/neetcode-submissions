class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #for each one, find the min of the n-1 and n-2
        #predefined arr = ?
        #equation = ?

        #cost = [1, 2, 3]
        #we can start with first 2 at [1, 2]
        #min cost for step 3 is min(n+n-1, n+n-2)
        #min cost for final step (4) is the min(n-1, n-2)

        n = len(cost)

        if n <= 2:
            return min(cost)

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        print(dp)
        return min(dp[-1], dp[-2]) 
