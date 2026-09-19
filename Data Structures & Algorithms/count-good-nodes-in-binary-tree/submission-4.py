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

        def dfs(root_val: int, max_greatest: int, cur_node: TreeNode) -> int:
            #base cases
            if not cur_node:
                return 0
            
            if cur_node.val >= root_val and cur_node.val >= max_greatest:
                    #continue
                return 1 + dfs(root_val, cur_node.val, cur_node.left) + dfs(root_val, cur_node.val, cur_node.right)
                
            
            return dfs(root_val, max_greatest, cur_node.left) + dfs(root_val, max_greatest, cur_node.right)
        
        return dfs(root.val, root.val, root)


            




        