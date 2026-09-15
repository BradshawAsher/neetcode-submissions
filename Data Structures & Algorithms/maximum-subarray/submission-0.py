class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_prefix = 0
        min_prefix = 0 #represents prefix sum before index 0 (an empty prefix)

        for num in nums:
            current_prefix += num
            #best subarray ending at current index

            max_sum  = max(max_sum, current_prefix - min_prefix)
            
            #update running minimum prefix sum seen so far
            min_prefix = min(min_prefix, current_prefix)

        return max_sum
