class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        max_len = -1
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        for i in range(len(s)):
            if i > 0:

                cur_len = 0
                left = i-1
                right = i
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_len += 2
                    left -= 1
                    right += 1
                
                if cur_len > max_len:
                    max_len = cur_len
                    output = s[left+1:right]


                cur_len = 1
                left = i-1
                right = i+1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_len += 2
                    left -= 1
                    right += 1
                
                if cur_len > max_len:
                    max_len = cur_len
                    output = s[left+1:right]

        return output
        
        
obj = Solution()
print(obj.longestPalindrome("a"))
print(obj.longestPalindrome("aa"))
print(obj.longestPalindrome("ccd"))
print(obj.longestPalindrome("babad"))
print(obj.longestPalindrome("cbbd"))