# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def add_node(self, cur_list):
        cur_list.next = ListNode()
        cur_list = cur_list.next
        return cur_list
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = ListNode()
        p_new = None
        p_l1 = list1
        p_l2 = list2
        while p_l1 or p_l2:
            if p_new == None:
                p_new = new_list
            else:
                p_new = self.add_node(p_new)

            # calculate sum
            if p_l1 and p_l2:
                if p_l1.val > p_l2.val:
                    p_new.val = p_l2.val
                    p_l2 = p_l2.next
                else:
                    p_new.val = p_l1.val
                    p_l1 = p_l1.next

            elif p_l1 and not p_l2:
                p_new.val = p_l1.val
                p_l1 = p_l1.next
            
            elif not p_l1 and p_l2:
                p_new.val = p_l2.val
                p_l2 = p_l2.next

        if p_new == None:
            return None
        return new_list