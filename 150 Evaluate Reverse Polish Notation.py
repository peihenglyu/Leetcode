class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                num_2 = float(stack.pop())
                num_1 = float(stack.pop())
                new_num = 0
                if token == '+':
                    new_num = num_1 + num_2
                if token == '-':
                    new_num = num_1 - num_2
                if token == '*':
                    new_num = num_1 * num_2
                if token == '/':
                    new_num = int(num_1 / num_2)
                stack.append(new_num)
        
        return int(stack[0])

obj = Solution()
print(obj.evalRPN(["2","1","+","3","*"]))
print(obj.evalRPN(["4","13","5","/","+"]))
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))