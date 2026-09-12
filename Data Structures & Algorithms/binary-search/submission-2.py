class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        #binary seasrch update equation is very important
        mid = len(nums) // 2

        left = 0
        right = len(nums)-1

        #need to update left and right based on char's position regarding mid, would always do left = mid+1 or right = mid-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while left <= right:
            cur = nums[mid]

            if cur == target:
                return mid
            
            elif cur < target:
                #too small, need to go up
                left = mid+1
            else:
                #cur > target
                #too large, need to go down
                right = mid-1

            #formula time
            mid = (left+right)//2
        
        return -1
        