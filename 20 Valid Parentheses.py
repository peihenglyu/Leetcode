class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for paren in s:
            if paren in ['(', '{', '[']:
                stack.append(paren)
            elif paren == ')':
                if len(stack)==0 or stack.pop() != '(':
                    return False
            elif paren == '}':
                if len(stack)==0 or stack.pop() != '{':
                    return False
            elif paren == ']':
                if len(stack)==0 or stack.pop() != '[':
                    return False
        if len(stack)==0:
            return True
        else:
            return False
