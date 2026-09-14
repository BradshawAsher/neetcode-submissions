class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_n: int, closed_n: int):
            #Base Case: we've placed all 2 * n parenthesis
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            #Branch 1: We can still place an opening bracket
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            #Branch 2: We can only place a closing bracket if it pairs with an open one
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res