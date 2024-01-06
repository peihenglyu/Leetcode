class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i_1 = 0
        i_2 = 0
        merge = ""
        while i_1 < len(word1) or i_2 < len(word2):
            if i_1 < len(word1) and i_2 < len(word2):
                merge += word1[i_1]
                merge += word2[i_2]
                i_1 += 1
                i_2 += 1
            elif i_1 < len(word1):
                merge += word1[i_1:]
                i_1 = len(word1)
            else:
                merge += word2[i_2:]
                i_2 = len(word2)
        
        return merge