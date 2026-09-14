from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #okay so we want to have a visited array
        #and then when we find a 1, continue exploring to find more
        #otherwise just have a nested for loop
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        num_islands = 0


        def explore(start_r: int, start_c: int):
            #essentially need to check bounds and then check for neighbors
            queue = deque([(start_r, start_c)])
            visited[start_r][start_c] = 1 #mark cell as visited

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                cur_r, cur_c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc

                    #check bounds, land, and not visited yet
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                        



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    #explore
                    num_islands += 1
                    explore(row, col)


        return num_islands
