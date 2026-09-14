from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid and not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        #1. add the treasure chests/gates (0s) to the queue initially
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        #level-order multi-source BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                #only visit in-bounds empty rooms (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        
