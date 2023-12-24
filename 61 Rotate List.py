# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            count = 1
            len_ptr = head
            while len_ptr.next:
                len_ptr = len_ptr.next
                count += 1
        else:
            return head
        
        shift = k % count

        if shift == 0:
            return head

        left_move = count - shift
        ptr = ListNode(next = head)
        while left_move:
            ptr = ptr.next
            left_move -= 1
        
        len_ptr.next = head
        new_head = ptr.next
        ptr.next = None

        return new_head
    
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
    print("\n")
    


obj = Solution()
LL_list = create_LList([1,2])
ite_LL(obj.rotateRight(LL_list, 1))
LL_list = create_LList([1,2,3,4,5])
ite_LL(obj.rotateRight(LL_list, 2))