class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index = 0
        pre = s[0]
        for i in range(len(p)):

            if p[i] != '.' and p[i] != '*':
                if s[s_index] != p[i]:
                    if i + 1 < len(p) and p[i + 1] == '*':
                        pre = p[i]
                    else:
                        return False
                else:
                    pre = p[i]
                    s_index += 1
                    if s_index >= len(s):
                        if i != len(p) - 1 and not (i + 1 == len(p)-1 and p[i+1] == "*"):
                            return False
                    
            elif p[i] == '.':
                pre = '.'
                s_index += 1
                if s_index >= len(s):
                    if i != len(p) - 1:
                        return False
            
            else:
                while s_index < len(s) and (pre == '.' or s[s_index] == pre):
                    s_index += 1
                    if s_index == len(s):
                        if i != len(p) - 1:
                            return False

        if s_index != len(s):
            return False
        
        return True

obj = Solution()
print(obj.isMatch("aa","a"))
print(obj.isMatch("aa","a*"))
print(obj.isMatch("aa",".*"))
print(obj.isMatch("ab",".*"))
print(obj.isMatch("aab","c*a*b*"))
print(obj.isMatch("aaabbbbbbbb","a*ab*bbbbb*"))