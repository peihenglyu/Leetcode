# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # Copy from 92. Reverse Linked List II
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        count = 1
        poi = head
        last_poi = None
        if right - left < 1:
            return head
        
        if right - left == 1:
            while count != left:
                last_poi = poi
                poi = poi.next
                count += 1

            next_poi = poi.next
            if last_poi != None:
                last_poi.next = next_poi
            else:
                head = next_poi
            poi.next = next_poi.next
            next_poi.next = poi
            

        else:
            node_list = []
            before_left = None
            after_right = None
            while poi:
                if count >= left and count <= right:
                    if count == left:
                        if last_poi != None:
                            before_left = last_poi
                    if count == right:
                        after_right = poi.next

                    node_list.append(poi)
                last_poi = poi
                poi = poi.next
                count += 1
            
            for i in range(len(node_list)):
                if i == 0:
                    if before_left != None:
                        before_left.next = node_list[-1]
                    else:
                        head = node_list[-1]
                    node_list[-1-i].next = node_list[-1-i-1]
                elif i == len(node_list)-1:
                    node_list[0].next = after_right
                else:
                    node_list[-1-i].next = node_list[-1-i-1]
        
        return head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        right_count = 1
        dummy = ListNode(0,head)
        pointer = dummy.next
        left = dummy
        first_reverse = True


        while pointer:
            if right_count == k:
                temp = left.next
                self.reverseBetween(left, 1 + 1, 1 + right_count)
                right_count = 1
                left = temp
                pointer = left.next
            else:
                count += 1
                right_count += 1
                pointer = pointer.next
        
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
print(obj.reverseKGroup(head, 2))