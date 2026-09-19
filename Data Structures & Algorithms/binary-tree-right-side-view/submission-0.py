# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #literally just a level-order traversal and then add the last one to res
        res = []
        if not root:
            return []

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == level_size-1:
                    res.append(node.val)
        
        return res


