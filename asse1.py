class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_dict ={}
        for word in words:
            cur_dict = {}
            for letter in word:
                if letter not in cur_dict:
                    if letter not in word_dict:
                        word_dict[letter] = [1]
                    else:
                        word_dict[letter][0] += 1
                    cur_dict[letter] = [1]
                else:
                    cur_dict[letter].append(1)
                    if len(word_dict[letter]) < len(cur_dict[letter]):
                        word_dict[letter].append(1)
                    else:
                        word_dict[letter][len(cur_dict[letter])-1] += 1
                    
        
        len_words = len(words)
        output = []
        for key in word_dict:
            for appear in word_dict[key]:
                if appear == len_words:
                    output.append(key)
        return output
                
obj = Solution()
print(obj.commonChars(["bella","label","roller"]))