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

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            #Base cases: out of bounds or not an "O"
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "S" #mark safe immediately

            #explore 4 neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        #Trigger DFS only from border cells
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == "O":
                    dfs(r, c)

        #Step 3: Single pass to flip trapped "O" -> "X" and restore safe "S" -> "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        
        return

