class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #keep the smaller dimension to minimize memory
        if m < n:
            m, n = n, m #m = 6, n = 3
        
        row = [1] * n

        for _ in range(m-1):
            for c in range(1, n):
                row[c] += row[c - 1]

        return row[-1]
        