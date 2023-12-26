class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        le_dict = {}
        for letter in s:
            if letter not in le_dict:
                le_dict[letter] = 1
            else:
                le_dict[letter] += 1
        
        for letter in t:
            if letter not in le_dict:
                return False
            else:
                le_dict[letter] -= 1

        for key in le_dict:
            if le_dict[key] != 0:
                return False
            
        return True