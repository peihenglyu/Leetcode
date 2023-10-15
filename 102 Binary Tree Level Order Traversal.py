# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        level_val = []
        cur_level = [root]
        cur_lever_val = []
        next_level = []
        while len(cur_level) > 0:
            while len(cur_level) > 0:
                cur_node = cur_level.pop(0)
                cur_lever_val.append(cur_node.val)
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
            level_val.append(cur_lever_val)
            cur_level = next_level
            next_level = []
            cur_lever_val = []

        return level_val