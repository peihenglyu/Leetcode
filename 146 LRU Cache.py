
class LRUCache(object):

    class LL_Node:
        def __init__(self, key, val = 0, next = None, prev = None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev
            
        

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.Node_dict = {}
        self.tail = self.LL_Node('tail')
        self.head = self.LL_Node('head')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.LL_len = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: intw
        """
        cur_dict = self.Node_dict

        if key in self.Node_dict:
            print(key)
            cur_node = self.Node_dict[key]

            cur_prev = cur_node.prev
            cur_next = cur_node.next
            cur_prev.next = cur_next
            cur_next.prev = cur_prev

            head_next = self.head.next
            self.head.next = cur_node
            cur_node.next = head_next
            head_next.prev = cur_node
            cur_node.prev = self.head

            return cur_node.val
        else:
            print(-1)
            return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        cur_dict = self.Node_dict

        if key in self.Node_dict:
            cur_node = self.Node_dict[key]
            cur_node.val = value
            self.get(key)
        else:
            if self.LL_len >= self.capacity:
                drop_key = self.tail.prev.key
                last_prev = self.tail.prev.prev
                last_prev.next = self.tail
                self.tail.prev = last_prev
                self.Node_dict.pop(drop_key)
                self.LL_len -= 1

            cur_node = self.LL_Node(key, value)
            self.Node_dict[key] = cur_node
            head_next = self.head.next
            self.head.next = cur_node
            cur_node.next = head_next
            head_next.prev = cur_node
            cur_node.prev = self.head
            self.LL_len += 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def test1():
    obj = LRUCache(2)
    param_1 = obj.get(1)
    obj.put(1,1)
    obj.put(2,2)
    param_1 = obj.get(1)
    obj.put(3,3)
    param_1 = obj.get(2)
    obj.put(4,4)
    param_1 = obj.get(1)
    param_1 = obj.get(3)
    param_1 = obj.get(4)


def test2():
    obj = LRUCache(2)
    param_1 = obj.get(1)
    obj.put(2,1)
    obj.put(2,2)
    param_1 = obj.get(2)
    obj.put(3,3)
    param_1 = obj.get(2)
    obj.put(4,4)
    param_1 = obj.get(1)
    param_1 = obj.get(3)
    param_1 = obj.get(4)

test2()