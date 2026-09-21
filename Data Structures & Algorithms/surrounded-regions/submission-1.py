from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #so essentially find all border O's.
        #mark them with an "S" for safe, and then do dfs/bfs to find any other Os they can reach.
        #after you processed all the S's, then all the Os inside turn back to Xs
        #so we will look for all O's on the border, then change to S. When we change to S, add to the queue, and then have a visited as well (2d matrix copy)
        #do we even need a visited or no? Or just can only go to Os, not X or S?

        #after we are doing, then go through the queue?
        
        if not board or not board[0]:
            return 

        queue = deque()

        rows, cols = len(board), len(board[0])

        #Step 1: Find all border O's and seed the multi-source queue
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == "O":
                    board[r][c] = "S"
                    queue.append((r, c))

        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S" #Mark safe immediately before enqueueing
                    queue.append((nr, nc))

        #Step 3: Single pass to flip trapped "O" -> "X" and restore safe "S" -> "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        
        return

