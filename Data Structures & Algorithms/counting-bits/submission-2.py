class Solution:
    def countBits(self, n: int) -> List[int]:
    
        dp = [0] * (n+1)

        for i in range(1, n+1):
            #1 + count of bits in i with its lowest set bit removed
            dp[i] = dp[i & (i-1)] + 1

        return dp

