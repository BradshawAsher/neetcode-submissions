class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        max_island_size = 0

        def dfs(start_r: int, start_c: int) -> int:
            #base case: out of bounds or water
            if start_r < 0 or start_r >= rows or start_c < 0 or start_c >= cols or grid[start_r][start_c] == 0 or visited[start_r][start_c]:
                return 0

            visited[start_r][start_c] = True

            return 1 + dfs(start_r-1, start_c) + dfs(start_r+1, start_c) + dfs(start_r, start_c+1) + dfs(start_r, start_c-1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    max_island_size = max(max_island_size, dfs(r, c))
        
        return max_island_size
