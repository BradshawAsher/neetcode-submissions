class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                #min must be to the right of mid
                left = mid + 1
            else:
                #nums[mid] <= nums[right]: min could be mid or to the left
                right = mid
        
        #left == right, pointing to the minimum element
        return nums[left]


