class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #for each one, find the min of the n-1 and n-2
        #predefined arr = ?
        #equation = ?

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        
        return min(prev1, prev2)
