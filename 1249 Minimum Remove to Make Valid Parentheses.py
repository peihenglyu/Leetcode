class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = []
        index = 1
        for index, l in enumerate(s):
            if l == '(':
                stack.append(index)
            elif l == ')':
                if len(stack):
                    stack.pop()
                else:
                    s[index] = '#'
            index += 1

        for i in stack:
            s[i] = '#'
        
        result = ''
        for l in s:
            if l != '#':
                result += l
        
        return result
    
obj = Solution()
print(obj.minRemoveToMakeValid("lee(t(c)o)de)"))
# print(obj.minRemoveToMakeValid("a)b(c)d"))
# print(obj.minRemoveToMakeValid("))(("))