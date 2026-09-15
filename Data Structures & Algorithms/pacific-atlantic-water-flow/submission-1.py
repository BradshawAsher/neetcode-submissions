from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #do it the bfs way
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_queue = deque()
        atl_queue = deque()

        pac_reachable = set()
        atl_reachable = set()

        #1. enqueue all the border cells
        for c in range(cols):
            pac_queue.append((0, c))
            pac_reachable.add((0, c))

            atl_queue.append((rows - 1, c))
            atl_reachable.add((rows - 1, c))
        
        for r in range(rows):
            pac_queue.append((r, 0))
            pac_reachable.add((r, 0))

            atl_queue.append((r, cols - 1))
            atl_reachable.add((r, cols - 1))
        
        #2. Shared BFS function moving uphill
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(queue: deque, reachable: set):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    #bounds check + unvisited + reverse uphill check
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable and heights[nr][nc] >= heights[r][c]):
                        reachable.add((nr, nc))
                        queue.append((nr, nc))
        
        bfs(pac_queue, pac_reachable)
        bfs(atl_queue, atl_reachable)

        #3. Intersection of reachable coordinates
        return [[r, c] for r, c in pac_reachable & atl_reachable]


