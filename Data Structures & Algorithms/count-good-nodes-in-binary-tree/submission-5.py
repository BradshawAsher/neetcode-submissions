# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #so essentially the root has to be smaller than target
        #and the mid value cannot be greater than the node

        #So in the first example we start at root 2, need to store the root
        #we go left and right, both smaller than 2, so we continue left and right exploring
        #and then if we mark a node good, then we have to store max_greatest for that specific path (dfs probably), and the next nodes only count if they are greater than the max_greatest parent
        #in example 2, 3 and 4 both count since they are siblings of the 2.

        def dfs(node: TreeNode, max_val: int) -> int:
            #base cases
            if not node:
                return 0
            
            #a node is good if its value >= max value on the path so far
            is_good = 1 if node.val >= max_val else 0

            new_max = max(max_val, node.val)
                
            
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)
        
        return dfs(root, root.val)


            




        