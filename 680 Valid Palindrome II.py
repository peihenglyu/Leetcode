class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        deleted = 0
        def test_pali(left_i, right_i):
            while left_i < right_i:
                if s[left_i] == s[right_i]:
                    left_i += 1
                    right_i -= 1
                else:
                    return False
            
            return True
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return test_pali(left+1, right) or test_pali(left, right-1)
        
        return True

obj = Solution()
print(obj.validPalindrome("eeccccbebaeeabebccceea"))
print(obj.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))