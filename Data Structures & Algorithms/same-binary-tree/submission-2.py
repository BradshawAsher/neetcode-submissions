# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            #both none at this branch -> continue checking rest of the queue
            if not node_p and not node_q:
                continue

            #one is none or values don't match -> trees are different
            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            #push left children pair and right children pair
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
        return True
