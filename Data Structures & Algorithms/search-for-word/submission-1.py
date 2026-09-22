class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #we can terminate if the cur_length is greater than the word length
        #backtracking is usually like a loop
        #like for dr, dc, in dir:
        #nr, nc = ...
        #dfs(nr, nc) something like that

        #input = 2d board
        #output = bool
        #match = backtracking
        #plan

        #loop through each item on the board and check for first word
        #if we hit first word, then enter backtracking?

        #Time = O(m*(4^n)) time and O(n) space, where m is # of cells and n is the size of given word

        #use a visited set for each backtracking thing?
        if not word:
            return True

        if not board or not board[0]:
            return False


        def dfs(r: int, c: int, cur_word: str, visited: set) -> bool:
            #check bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            #have to compare most recent character
            
            if len(cur_word) == len(word):
                return cur_word == word

            if word[len(cur_word) - 1] != cur_word[-1]:
                return False
            
            target_char = word[len(cur_word)]
            #look for target char
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    cur = board[nr][nc]
                    visited.add((nr, nc))
                    if dfs(nr, nc, cur_word+cur, visited):
                        return True
                    visited.remove((nr, nc)) #backtrack

            return False 



        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                cur = board[r][c]
                if cur == word[0]:
                    if dfs(r, c, cur, {(r, c)}):
                        return True

        return False




