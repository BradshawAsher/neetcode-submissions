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

        queue = deque([])

        rows, cols = len(board), len(board[0])

        #first find all the border O's

        #first top and bottom
        for r in [0, rows-1]:
            for c in range(cols):
                if board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "S"
        
        #now left and right
        for c in [0, cols-1]:
            for r in range(rows):
                if board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "S"

        
        #now go through queue and do bfs through the whole queue starting from all those points
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()

            cur_queue = deque([(r, c)])

            while cur_queue:
                cur_r, cur_c = cur_queue.popleft()

                #check bounds and stuff
                for dr, dc, in directions:
                    nr, nc = cur_r+dr, cur_c+dc

                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        #continue
                        board[nr][nc] = "S"
                        cur_queue.append((nr, nc))

        #now go through the board again and mark all O's that are not S's as X.
        #then go back through and mark all S's as an O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
        
        return





        





        #O(m*n) time and O(m*n) space