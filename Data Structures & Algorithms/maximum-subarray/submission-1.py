class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def find_max(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2

            #1. best subarray strictly in the left half
            left_best = find_max(left, mid)

            #2. best subarray strictly in the right half
            right_best = find_max(mid + 1, right)

            #3. expand subarray crossing the midpoint:
            #expand left from mid
            left_cross_max = float("-inf")
            running_sum = 0

            for i in range(mid, left - 1, -1):
                running_sum += nums[i]
                left_cross_max = max(left_cross_max, running_sum)

            #expand right from mid + 1
            right_cross_max = float("-inf")
            running_sum = 0

            for i in range(mid + 1, right + 1):
                running_sum += nums[i]
                right_cross_max = max(right_cross_max, running_sum)

            cross_best = left_cross_max + right_cross_max

            return max(left_best, right_best, cross_best)

        return find_max(0, len(nums) - 1)
