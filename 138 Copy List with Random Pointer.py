"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        count = 0
        last_node = None
        new_list = None
        pointer = head
        dict = {}
        while pointer:
            if new_list == None:
                node = Node(pointer.val)
                dict[pointer] = node
                pointer = pointer.next

                new_list = node
                last_node = node
                count += 1

            else:
                node = Node(pointer.val)
                dict[pointer] = node
                pointer = pointer.next

                last_node.next = node
                last_node = node
                count += 1
        
        pointer_new = new_list
        pointer = head
        while pointer_new:
            if pointer.random == None:
                pointer_new.random = None
            else:
                pointer_new.random = dict[pointer.random]
            
            pointer_new = pointer_new.next
            pointer = pointer.next
        
        return new_list