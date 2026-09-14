class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current: str, open_n: int, closed_n: int):
            if len(current) == 2*n:
                res.append(current)
                return

            if open_n < n:
                backtrack(current + "(", open_n+1, closed_n)
            if closed_n < open_n:
                backtrack(current + ")", open_n, closed_n+1)

        backtrack("", 0, 0)
        return res