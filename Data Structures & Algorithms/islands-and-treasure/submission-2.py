from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        # 1. Enqueue all gates (0s) simultaneously
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # 2. Concentric expansion (multi-source BFS)
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                # Only proceed into in-bounds unvisited rooms (INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))