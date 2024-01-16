# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head


        def merge(head_1, head_2):
            dummy = ListNode()
            ptr = dummy
            while head_1 or head_2:
                if not head_1:
                    ptr.next = head_2
                    break
                elif not head_2:
                    ptr.next = head_1
                    break
                elif head_1.val > head_2.val:
                    ptr.next = head_2
                    head_2 = head_2.next
                    ptr = ptr.next
                else:
                    ptr.next = head_1
                    head_1 = head_1.next
                    ptr = ptr.next
            return dummy.next
        
        def solver(head):
            if not head.next:
                    return head
            if not head.next.next:
                if head.val > head.next.val:
                    new_head = head.next
                    head.next = None
                    new_head.next = head
                    return new_head
                else:
                    head.next.next = None
                    return head
            else:
                fast_ptr = head
                slow_ptr = head
                while fast_ptr:
                    fast_ptr = fast_ptr.next
                    if fast_ptr:
                        fast_ptr = fast_ptr.next
                        slow_ptr = slow_ptr.next
                
                temp = slow_ptr.next
                slow_ptr.next = None
                    
                return merge(solver(head), solver(temp))
        
        return solver(head)
                

head = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
head_2 = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))

obj = Solution()

def print_LL(head):
    s = []
    while head:
        s.append(head.val)
        head = head.next
    print(s)

print_LL(obj.sortList(head))
print_LL(obj.sortList(head_2))
        
                