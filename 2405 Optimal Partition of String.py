class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        count = 0
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                count += 1
                dict = {}
                dict[s[i]] = 1
        return count + 1