class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #essentially make as many combinations as possible can reuse, but terminate if the sum goes above target
        nums.sort() #allows early exit
        res = []
        subset = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                res.append(subset.copy())

            for j in range(start, len(nums)):
                if nums[j] > remaining:
                    break #stop since array is sorted

                subset.append(nums[j])
                backtrack(j, remaining - nums[j]) #stay at j to allow reuse
                subset.pop()

        backtrack(0, target)
        return res