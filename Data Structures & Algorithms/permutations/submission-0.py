class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #backtracking
        #3*2*1
        #each number will start at the front len(nums)-1 times
        res = []
        perm = []
        visited = set()

        def backtrack():
            #base case: we filled all the slots
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in visited:
                    continue

                #1. make choice
                visited.add(num)
                perm.append(num)

                #2. explore deeper
                backtrack()

                #3. undo choice (backtrack)
                perm.pop()
                visited.remove(num)
        backtrack()
        return res
        