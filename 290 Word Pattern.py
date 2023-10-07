class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_words = s.split()
        if len(s_words)!= len(pattern):
            return False
        n = len(s_words)
        dict_1 = {}
        dict_2 = {}
        patten_1 = ""
        patten_2 = ""
        count_1 = 0
        count_2 = 0
        for i in range(n):
            word_s = s_words[i]
            letter_t = pattern[i]
            if word_s in dict_1:
                patten_1 += dict_1[word_s]
            else:
                dict_1[word_s] = str(count_1)
                count_1 += 1
            
            if letter_t in dict_2:
                patten_2 += dict_2[letter_t]
            else:
                dict_2[letter_t] = str(count_2)
                count_2 += 1

            if patten_1 != patten_2:
                return False
        return True