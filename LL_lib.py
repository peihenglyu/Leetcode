class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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