class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.min_list) == 0:
            self.min_list.append(0)
        elif val < self.stack[self.min_list[-1]]:
            self.min_list.append(len(self.stack))
        else:
            self.min_list.append(self.min_list[-1])
        self.stack.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.min_list[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
obj.top()
obj.getMin()