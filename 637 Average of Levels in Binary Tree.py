# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        average = []
        cur_level = [root]
        next_level = []
        while len(cur_level) > 0:
            sum = 0
            count = 0
            while len(cur_level) > 0:
                cur_node = cur_level.pop(0)
                sum += cur_node.val
                count += 1
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
            average.append(sum/float(count))
            cur_level = next_level
            next_level = []

        return average