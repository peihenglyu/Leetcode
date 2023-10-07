class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        n = len(s)
        dict_1 = {}
        dict_2 = {}
        patten_1 = ""
        patten_2 = ""
        count_1 = 0
        count_2 = 0
        for i in range(n):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s in dict_1:
                patten_1 += dict_1[letter_s]
            else:
                dict_1[letter_s] = str(count_1)
                count_1 += 1
            
            if letter_t in dict_2:
                patten_2 += dict_2[letter_t]
            else:
                dict_2[letter_t] = str(count_2)
                count_2 += 1

            if patten_1 != patten_2:
                return False
        return True
                
            
