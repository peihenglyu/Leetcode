class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_nodes = [root]
        while len(cur_nodes):
            next_nodes = []
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if not len(next_nodes):
                sum = 0
                for node in cur_nodes:
                    sum += node.val
                return sum
            else:
                cur_nodes = next_nodes

root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(6, None, None)))
obj = Solution()
print(obj.deepestLeavesSum(root))