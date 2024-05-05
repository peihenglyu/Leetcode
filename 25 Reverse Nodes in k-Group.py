# My first Solution
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     # Copy from 92. Reverse Linked List II
#     def reverseBetween(self, head, left, right):
#         """
#         :type head: ListNode
#         :type left: int
#         :type right: int
#         :rtype: ListNode
#         """
#         count = 1
#         poi = head
#         last_poi = None
#         if right - left < 1:
#             return head
        
#         if right - left == 1:
#             while count != left:
#                 last_poi = poi
#                 poi = poi.next
#                 count += 1

#             next_poi = poi.next
#             if last_poi != None:
#                 last_poi.next = next_poi
#             else:
#                 head = next_poi
#             poi.next = next_poi.next
#             next_poi.next = poi
            

#         else:
#             node_list = []
#             before_left = None
#             after_right = None
#             while poi:
#                 if count >= left and count <= right:
#                     if count == left:
#                         if last_poi != None:
#                             before_left = last_poi
#                     if count == right:
#                         after_right = poi.next

#                     node_list.append(poi)
#                 last_poi = poi
#                 poi = poi.next
#                 count += 1
            
#             for i in range(len(node_list)):
#                 if i == 0:
#                     if before_left != None:
#                         before_left.next = node_list[-1]
#                     else:
#                         head = node_list[-1]
#                     node_list[-1-i].next = node_list[-1-i-1]
#                 elif i == len(node_list)-1:
#                     node_list[0].next = after_right
#                 else:
#                     node_list[-1-i].next = node_list[-1-i-1]
        
#         return head

#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         count = 1
#         right_count = 1
#         dummy = ListNode(0,head)
#         pointer = dummy.next
#         left = dummy
#         first_reverse = True


#         while pointer:
#             if right_count == k:
#                 temp = left.next
#                 self.reverseBetween(left, 1 + 1, 1 + right_count)
#                 right_count = 1
#                 left = temp
#                 pointer = left.next
#             else:
#                 count += 1
#                 right_count += 1
#                 pointer = pointer.next
        
#         return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My second solution with O(1) space complexity
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        dummy = ListNode(0, head)
        ptr = dummy
        k_count = 0
        end_of_front = None
        last_starter = None
        while ptr != None:
            if k_count == 0:
                end_of_front = ptr
                last_starter = ptr.next
                last_node = ptr
                ptr = ptr.next
                k_count += 1
            elif k_count > 0 and k_count < k:
                next_node = ptr.next
                ptr.next = last_node
                last_node = ptr
                ptr = next_node
                k_count += 1
            elif k_count == k:
                next_node = ptr.next
                end_of_front.next = ptr
                last_starter.next = next_node
                ptr.next = last_node
                ptr = last_starter
                k_count = 0
        
        bacK_last_node = None
        # print(k_count)
        if k_count != 0:
            ptr = last_node
            while ptr != end_of_front:
                next_node = ptr.next
                ptr.next = bacK_last_node
                bacK_last_node = ptr
                ptr = next_node
                k_count -= 1
        
        return dummy.next

def print_LL(head):
    while head != None:
        print(head.val)
        head = head.next

head = ListNode(1)
cur_poi = head
cur_poi.next = ListNode(2)
cur_poi = cur_poi.next
cur_poi.next = ListNode(3)
cur_poi = cur_poi.next
cur_poi.next = ListNode(4)
cur_poi = cur_poi.next
cur_poi.next = ListNode(5)
cur_poi = cur_poi.next
obj = Solution()
ll1 = obj.reverseKGroup(head, 2)
print_LL(ll1)
# print()