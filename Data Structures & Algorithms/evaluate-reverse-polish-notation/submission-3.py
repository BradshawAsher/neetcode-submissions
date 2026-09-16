import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack
        #U - Understand
        #Input = tokens -> list of strs
        #output = int for result
        
        #match - stack

        #plan 
        #so can't you just process 2 numbers at a time with an operand, and then replace 2 with 1? in the stack

        stack = []

        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a/b)}

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
