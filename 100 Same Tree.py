# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (q == None and p != None):
            return False
        elif p == q == None:
            return True
        else:
            cur_same = (p.val == q.val)
            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)
            return cur_same and left_same and right_same
        
# # better Solution:
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         if (p == None and q != None) or (q == None and p != None):
#             return False
#         elif p == q == None:
#             return True
#         else:
#             cur_same = (p.val == q.val)
#             left_same = self.isSameTree(p.left, q.left)
#             right_same = self.isSameTree(p.right, q.right)
#             return cur_same and left_same and right_same