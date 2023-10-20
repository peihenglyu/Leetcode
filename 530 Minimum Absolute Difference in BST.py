# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDiff = self.find_min(root)[2]
        return minDiff
        
    def find_min(self, root):
        if not root:
            return (float('inf'),float('-inf'), float('inf'))
        
        left = self.find_min(root.left)
        right = self.find_min(root.right)
        minDiff = min(left[2], right[2], abs(root.val - left[1]), abs(root.val - right[0]))
        return (min(root.val, left[0]), max(root.val,right[1]), minDiff)
