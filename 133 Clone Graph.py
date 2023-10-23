"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        node_dict = {}
        origin_dict = {}
        node_list = []
        if node:
            node_list.append(node)
        else:
            return None
        while len(node_list):
            cur_node = node_list.pop()
            if cur_node.val not in node_dict:
                origin_dict[cur_node.val] = cur_node
                node_dict[cur_node.val] = Node(val = cur_node.val)
                neighbors = cur_node.neighbors
                for i in range(len(neighbors)):
                    if neighbors[i].val not in node_dict:
                        node_list.append(neighbors[i])
        
        for key in origin_dict:
            for i in range(len(origin_dict[key].neighbors)):
                node_dict[key].neighbors.append(node_dict[(origin_dict[key].neighbors)[i].val])

        return node_dict[1]

node_1 = Node(val = 1)
node_2 = Node(val = 2)
node_3 = Node(val = 3)
node_4 = Node(val = 4)
node_1.neighbors = [node_2, node_4]
node_2.neighbors = [node_1, node_3]
node_3.neighbors = [node_2, node_4]
node_4.neighbors = [node_1, node_3]

obj = Solution()
print(obj.cloneGraph(node_1))