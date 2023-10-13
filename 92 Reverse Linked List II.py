# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
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
                poi = poi.next
                count += 1

            next_poi = poi.next
            if last_poi != None:
                last_poi.next = next_poi
            else:
                head = next_poi
            poi.next = next_poi.next
            next_poi.next = poi
            last_poi = poi

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

head = ListNode(3)
cur_poi = head
cur_poi.next = ListNode(5)
# cur_poi = cur_poi.next
# cur_poi.next = ListNode(3)
# cur_poi = cur_poi.next
# cur_poi.next = ListNode(4)
# cur_poi = cur_poi.next
# cur_poi.next = ListNode(5)
# cur_poi = cur_poi.next
left = 1
right = 2
obj = Solution()
print(obj.reverseBetween(head, left, right))