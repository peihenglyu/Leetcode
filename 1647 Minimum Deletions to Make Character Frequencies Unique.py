import bisect

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        
        dict_count = {}
        min_count = 0
        dele = 0
        for key in dict_s:
            cur_count = dict_s[key]
            if cur_count not in dict_count:
                dict_count[cur_count] = 1
            else:
                if cur_count < min_count:
                    dele += cur_count
                else:
                    temp = cur_count
                    while temp in dict_count and temp != 0:
                        temp -= 1
                        dele += 1
                    if temp == 0:
                        min_count = cur_count
                    else:
                        dict_count[temp] = 1
        
        return dele





aaaabbbbcccddeeeerrrrttttyyyy