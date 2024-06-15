# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def rightSideView(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if not root:
#             return None
#         right_side = [root.val]
#         cur_level = [root]
#         next_level = []
#         while len(cur_level) > 0:
#             while len(cur_level) > 0:
#                 cur_node = cur_level.pop(0)
#                 if cur_node.left:
#                     next_level.append(cur_node.left)
#                 if cur_node.right:
#                     next_level.append(cur_node.right)
#             if len(next_level) > 0:
#                 right_side.append(next_level[-1].val)
#             cur_level = next_level
#             next_level = []

#         return right_side

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        cur_stack = [root]
        result = []
        while len(cur_stack):
            result.append(cur_stack[-1].val)
            next_stack = []
            for node in cur_stack:
                if node.left or node.right:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)

            cur_stack = next_stack
        
        return result

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
obj = Solution()
print(obj.rightSideView(root))