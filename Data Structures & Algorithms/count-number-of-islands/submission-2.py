from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #okay so we want to have a visited array
        #and then when we find a 1, continue exploring to find more
        if not grid or not grid[0]:
            return 0


        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        num_islands = 0

        def dfs(r: int, c: int):
            #Base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1" or visited[r][c]:
                return
            
            #mark as visited
            visited[r][c] = True

            #visit all 4 adjacent neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    num_islands += 1
                    dfs(r, c)

        return num_islands