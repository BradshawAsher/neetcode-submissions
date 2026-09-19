# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #Queue stores tuples: (current_node, min_allowed, max_allowed)
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, low, high = queue.popleft()

            #The current node must strictly satisfy low < val < high
            if not (low < node.val < high):
                return False

            #Left child must be in (low, node.val)
            if node.left:
                queue.append((node.left, low, node.val))

            #Right child must be in (node.val, high)
            if node.right:
                queue.append((node.right, node.val, high))

        return True
            


