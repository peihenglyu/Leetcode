class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        count = 0
        letter_dict = {}
        left = 0
        for i in range(len(s)):
            cur_letter = s[i]
            if s[i] not in letter_dict:
                count += 1
                letter_dict[cur_letter] = 1
                if count >= max_count:
                    max_count = count
            else:
                while s[left] != cur_letter:
                    letter_dict.pop(s[left])
                    count -= 1
                    left += 1
                left += 1
        
        return max_count


obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkew"))