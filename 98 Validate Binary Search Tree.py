# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        test_left = True
        test_right = True
        if root.left:
            if root.left.val >= root.val:
                test_left = False
        if root.right:
            if root.right.val <= root.val:
                test_right = False
        return self.isValidBST(root.left) and self.isValidBST(root.right) and test_left and test_right
