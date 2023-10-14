# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_list, right_list = [],[]
        left_list.append(root.left)
        right_list.append(root.right)
        while len(left_list) or len(right_list):
            node_left = left_list.pop(0)
            node_right = right_list.pop(0)
            if node_left and node_right and node_left.val == node_right.val:
                left_list.append(node_left.left)
                left_list.append(node_left.right)
                right_list.append(node_right.right)
                right_list.append(node_right.left)
            else:
                if node_left != node_right:
                    return False
        
        return True