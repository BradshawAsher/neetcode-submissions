class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r: int, c: int, reachable_set: set):
            reachable_set.add((r, c))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                #check the bounds, unvisited in this set, and flow condition (UPHILL)
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable_set and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable_set)

        #1. Start DFS along the ocean borders
        for c in range(cols):
            dfs(0, c, pac_reachable) #top edge (pacific)
            dfs(rows-1, c, atl_reachable) #bottom edge (atlantic)

        for r in range(rows):
            dfs(r, 0, pac_reachable) #left edge (pacific)
            dfs(r, cols-1, atl_reachable) #right edge (atlantic)

        #2. return intersection where water flows to both
        return [[r, c] for r, c in pac_reachable & atl_reachable]


