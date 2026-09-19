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
            res.append(queue[0].val)

            for i in range(len(queue)):
                node = queue.popleft()

                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
                

        return res


