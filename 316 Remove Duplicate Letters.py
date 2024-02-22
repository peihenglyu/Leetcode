class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos_dict = {}
        output = []
        # for index, letter in enumerate(s[::-1]):
        #     if letter not in pos_dict:
        #         output.append(letter)
        #         pos_dict[letter] = len(output)-1
        #     else:
        #         if letter < output[-1]:
        #             last_index = pos_dict[letter]
        #             output[last_index] = None
        #             output.append(letter)
        #             pos_dict[letter] = len(output)-1
        
        # output = [letter for letter in output if letter != None]
        # return "".join(output[::-1])
        index = 0
        track_set = set()
        cur_set = set()
        last_letter = None
        while index < len(s):
            letter = s[index]
            if last_letter == None:
                last_letter = letter
            else:
                if letter > last_letter:
                    track_set.add(letter)
            if letter not in pos_dict:
                output.append(letter)
                pos_dict[letter] = len(output)-1


obj = Solution()
print(obj.removeDuplicateLetters("abacb"))
# print(obj.removeDuplicateLetters("bcabc"))
# print(obj.removeDuplicateLetters("cbacdcbc"))
# print(obj.removeDuplicateLetters("cdadabcc"))