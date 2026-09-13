class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 #if the last bit is 1, else 0
            n >>= 1 #logical right shift
        return count