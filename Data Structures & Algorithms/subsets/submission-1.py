class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start: int):
            #every state we reach is a valid subset
            res.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop() #backtrack

        backtrack(0)
        return res        