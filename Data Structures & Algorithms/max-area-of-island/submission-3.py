from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        #visited = [[False] * cols for _ in range(rows)]
        max_island_size = 0

        #do it the bfs way
        def bfs(start_r: int, start_c: int) -> int:
            queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = 0

            cur_island_size = 0
            #explore neighbors
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                cur_island_size += 1

                cur_r, cur_c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = cur_r + dr, cur_c + dc

                    #check bounds
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

            return cur_island_size


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    
                    max_island_size = max(bfs(r, c), max_island_size)
        
        return max_island_size