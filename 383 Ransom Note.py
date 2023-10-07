class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for letter in magazine:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        for letter in ransomNote:
            if letter in dict:
                dict[letter] -= 1
                if dict[letter] < 0:
                    return False
            else:
                return False
        
        return True