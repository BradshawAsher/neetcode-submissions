class Solution:
    def isValid(self, s: str) -> bool:
        #use a stack
        #keep on adding to the stack until you find a closer
        #then pop out from the stack and return true if stack is empty
        #if we find a closer but the top of stack is not complement, then return False
        mappings = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            #if opening, then add
            if char in mappings.values():
                stack.append(char)
            
            else:
                #if stack is empty or top doesn't match, then return False
                if not stack:
                    return False
                
                if stack[-1] != mappings.get(char):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
        