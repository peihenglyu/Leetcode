# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # My solution
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         def helper(root):
#             if not root:
#                 return (True, float('inf'), float('-inf'))
            
#             test_left = True
#             test_right = True

#             left = helper(root.left)
#             right = helper(root.right)

#             if root.val <= left[2]:
#                 test_left =  False

#             if root.val >= right[1]:
#                 test_right = False

#             return ( (test_left and test_right and left[0] and right[0]), min(root.val, left[1]), max(root.val, right[2]) )
#         return helper(root)[0]

# Better solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True 
            
            val=node.val
            if val<=lower or val>=upper:
                return False 

            return dfs(node.left,lower,val) and dfs(node.right,val, upper)
            
        
        return dfs(root)