# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        pre_idx = 0
        in_idx = 0

        def build(stop: Optional[int]) -> Optional[TreeNode]:
            nonlocal pre_idx, in_idx

            if pre_idx >= len(preorder):
                return None
            if inorder[in_idx] == stop:
                in_idx += 1
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            #left child cannot go past the current root_val
            root.left = build(root_val)
            #right child inherits the current level's stop boundary
            root.right = build(stop)

            return root

        return build(None)
