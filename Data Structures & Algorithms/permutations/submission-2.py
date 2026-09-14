class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        #3*2*1
        #each number will start at the front len(nums)-1 times
        res = []
        perm = []

        used = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                
                    backtrack()

                    perm.pop()
                    used[i] = False

        backtrack()
        return res