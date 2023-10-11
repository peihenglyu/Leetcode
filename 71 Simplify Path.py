class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        output = "/"
        path = path.split('/')
        path = [x for x in path if (x != "" and x != ".")]
        for i in path:
            if i == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(i)

        for i in range(len(stack)):
            if i != len(stack) -1:
                output += stack[i] + "/"
            else:
                output += stack[i]
            
        return output