class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        #3*2*1
        #each number will start at the front len(nums)-1 times
        res = []

        def backtrack(start: int):
            if start == len(nums):
                res.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] #swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start] #undo swap
        
        backtrack(0)
        return res
        