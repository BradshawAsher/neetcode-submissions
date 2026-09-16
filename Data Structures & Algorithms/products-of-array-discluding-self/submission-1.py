class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        #1. Forward pass: compute prefix products
        #res[i] will contain the product of all elements to the left of i
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #2. Backward pass: multiply by postfix products
        #postfix accumulates the product of all elements to the right of i
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res