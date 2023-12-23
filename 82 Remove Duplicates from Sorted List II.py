# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next = head)
        left_ptr = dummy
        right_ptr = head

        if not head:
            return None

        last_value = head.val
        dup_count = 1
        while right_ptr:
            right_ptr = right_ptr.next
            if right_ptr:
                if right_ptr.val != last_value:
                    if dup_count == 1:
                        left_ptr = left_ptr.next
                    last_value = right_ptr.val
                    dup_count = 1
                else:
                    dup_count += 1
                    left_ptr.next = right_ptr.next

        return dummy.next


def create_LList(nodes):
    head = ListNode(val = nodes[0])
    ptr = head
    for value in nodes[1:]:
        ptr.next = ListNode(val = value)
        ptr = ptr.next
    return head

def ite_LL(head):
    while head:
        print(head.val)
        head = head.next

obj = Solution()
LList = create_LList([1,2,3,3,4,4,5])
ite_LL(obj.deleteDuplicates(LList))
LList = create_LList([1,1,1,2,3])
ite_LL(obj.deleteDuplicates(LList))