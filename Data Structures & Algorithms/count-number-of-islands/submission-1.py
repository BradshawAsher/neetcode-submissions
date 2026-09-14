from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #okay so we want to have a visited array
        #and then when we find a 1, continue exploring to find more
        #otherwise just have a nested for loop
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0" #sink the island cell

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)

        return num_islands

