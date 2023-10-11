# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dict = {}
        pointer = head
        while pointer:
            if pointer in dict:
                return True
            else:
                dict[pointer] = 1
            pointer = pointer.next
        
        return False