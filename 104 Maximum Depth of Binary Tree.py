# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            left_depth = 0
            right_depth = 0
            if not root.left and not root.right:
                return 1
            if root.left:
                left_depth =  1 + self.maxDepth(root.left)
            if root.right:
                right_depth = 1 + self.maxDepth(root.right)

            return max(left_depth,right_depth)
        return 0
    