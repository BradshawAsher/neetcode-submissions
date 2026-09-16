class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        #We don't need to check the last element becuase once we reach it,
        #we have already arrived

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            #when we reach the boundary of our current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                #early exit if we can already reach or pass the end
                if current_end >= len(nums) - 1:
                    break
        
        return jumps

            