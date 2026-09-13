class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            #shift res left by 1 to make space, then insert the last bit of n
            res = (res << 1) | (n & 1)

            #drop the last bit of n
            n >>= 1

        return res