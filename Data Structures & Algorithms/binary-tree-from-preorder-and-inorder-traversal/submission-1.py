# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = stack[-1]

            if node.val != inorder[in_idx]:
                #As long as the top of the stack doesn't match inorder, 
                #we are still diving down the left side
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                #We've hit the leftmost node. Pop up to find which ancestor's 
                #right subtree we are entering
                while stack and stack[-1].val == inorder[in_idx]:
                    node = stack.pop()
                    in_idx += 1
                node.right = TreeNode(val)
                stack.append(node.right)

        return root
