class Solution:
    def climbStairs(self, n: int) -> int:
        #start from beginning (low) to end (large)
        #what is the dp formula?
        one, two = 1, 1

        for _ in range(n-1):
            temp = one
            one = one+two
            two = temp

        return one