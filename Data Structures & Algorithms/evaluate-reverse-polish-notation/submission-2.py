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

        operands = ["+", "*", "-", "/"]

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    new_token = first + second
                    stack.append(new_token)
                elif token == "*":
                    new_token = first * second
                    stack.append(new_token)
                elif token == "-":
                    new_token = first - second
                    stack.append(new_token)
                else:
                    #token == "/"
                    stack.append(int(first / second))
        
        return stack[-1]
