import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums) - k #Index in sorted array

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot_val = nums[pivot_idx]

            #1. Move pivot to the end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            #2. Move all elements <= pivot_val to the left side
            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot_val:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            #3. Move pivot to its final resting place
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx

        left, right = 0, len(nums) - 1
        
        while left <= right:
            #Pick a random pivot to avoid O(N^2) on pre-sorted arrays
            pivot_idx = random.randint(left, right)
            final_pivot_idx = partition(left, right, pivot_idx)

            if final_pivot_idx == target_idx:
                return nums[final_pivot_idx]

            elif final_pivot_idx < target_idx:
                left = final_pivot_idx + 1 #target is in the right half
            else:
                right = final_pivot_idx - 1 #target is in the left half

        return -1


