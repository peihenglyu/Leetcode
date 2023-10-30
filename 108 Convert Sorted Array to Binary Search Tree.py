# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 3:
            node_val = nums[len(nums)//2]
            node = TreeNode(val = node_val)
            nums.remove(nums[len(nums)//2])
            for rest in nums:
                if rest < node_val:
                    node_left = TreeNode(val = rest)
                    node.left = node_left
                if rest > node_val:
                    node_right = TreeNode(val = rest)
                    node.right = node_right
            return node
        else:
            pivot = len(nums)//2
            return TreeNode(val = nums[pivot], left = self.sortedArrayToBST(nums[:pivot]), right = self.sortedArrayToBST(nums[pivot+1:]))

nums =[3,5,8]
obj = Solution()
print(obj.sortedArrayToBST(nums))