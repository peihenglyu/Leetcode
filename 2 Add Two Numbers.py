# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode()
        p_new = None
        p_l1 = l1
        p_l2 = l2
        flag_add_one = 0
        while p_l1 or p_l2 or flag_add_one:
            new_num = 0

            # calculate sum
            if p_l1 and p_l2:
                new_num = p_l1.val + p_l2.val + flag_add_one
                if new_num >= 10:
                    new_num = new_num%10
                    flag_add_one = 1
                else:
                    flag_add_one = 0
                p_l1 = p_l1.next
                p_l2 = p_l2.next

            elif p_l1 and not p_l2:
                new_num = p_l1.val + flag_add_one
                if new_num >= 10:
                    new_num = new_num%10
                    flag_add_one = 1
                else:
                    flag_add_one = 0
                p_l1 = p_l1.next
            
            elif not p_l1 and p_l2:
                new_num = p_l2.val + flag_add_one
                if new_num >= 10:
                    new_num = new_num%10
                    flag_add_one = 1
                else:
                    flag_add_one = 0
                p_l2 = p_l2.next
            
            else:
                new_num = 1
                flag_add_one = 0
            
            # update linked list
            if p_new == None:
                p_new = new_list
                p_new.val = new_num
            else:
                p_new.next = ListNode()
                p_new = p_new.next
                p_new.val = new_num
            
        return new_list