from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #this is very similar to walls and gates and number of islands
        #first do a nested for loop to find the rotten fruit, add to queue
        #then have another while loop to go through the queue and explore the rotten fruit and simulate until there are nothing left in the queue
        #return if any fresh fruit left

        if not grid or not grid[0]:
            return 0

        time_taken = 0
        fresh_count = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        #1. count fresh oranges and enqueue all initially rotten ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

                elif grid[r][c] == 1:
                    fresh_count += 1

        #edge case: no fresh oranges exist
        if fresh_count == 0:
            return 0
                

        #now a while loop
        while queue and fresh_count > 0:
            #have to do level order traversal
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                #explore neighbors
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    #check bounds
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        #explore
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

            time_taken += 1
        
        return time_taken if fresh_count == 0 else -1


        
        