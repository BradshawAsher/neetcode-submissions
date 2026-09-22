from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        #1. Quick length check
        if len(word) > rows * cols:
            return False
        
        #2. Character frequency pruning
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)

        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        #3. Direct optimization: reverse word if prefix is denser than suffix
        #e.g. if word is "AAAAB", searching for "B" first avoids massive dead-end branching
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
        


        def dfs(r: int, c: int, i: int) -> bool:
            #Base case: matched all characters
            if i == len(word):
                return True

            #Boundary and characters match check
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            #Mark cell as visited in-place
            temp = board[r][c]
            board[r][c] = "#"

            #Explore all 4 neighbors
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1))

            #Backtrack: restore cell
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False




