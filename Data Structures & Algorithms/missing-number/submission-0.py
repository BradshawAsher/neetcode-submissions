class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #0 = 0000
        #1 = 0001
        #2 = 0010
        #3 = 0011
        #might be an xor
        res = len(nums) #initialize with n

        for i, num in enumerate(nums):
            #XOR the expected index/number with the actual value in the array
            res ^= i ^ num #res = res ^ (i ^ num)

        return res
