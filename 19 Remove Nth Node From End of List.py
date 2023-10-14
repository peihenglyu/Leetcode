# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        pointer = dummy
        left = dummy
        count = 1

        while pointer:
            if count <= n+1:
                pointer = pointer.next
                count += 1
            else:
                pointer = pointer.next
                left = left.next
        
        left.next = left.next.next
        return dummy.next
    
head = ListNode(3)
cur_poi = head
cur_poi.next = ListNode(5)
cur_poi = cur_poi.next
cur_poi.next = ListNode(3)
cur_poi = cur_poi.next
cur_poi.next = ListNode(4)
cur_poi = cur_poi.next
cur_poi.next = ListNode(5)
cur_poi = cur_poi.next
obj = Solution()
print(obj.removeNthFromEnd(head, 2))