class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_list = []
        def solver(root, level):
            if not root:
                return
            if len(max_list) <= level:
                max_list.append(float('-inf'))
            max_list[level] = max(root.val, max_list[level])
            solver(root.left, level+1)
            solver(root.right, level+1)

        solver(root, 0)
        
        return max_list

obj = Solution()
print(obj.largestValues())