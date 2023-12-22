class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        
        words_len = len(words[0])
        words_set = set(words)
        output = []
        left = 0
        right = words_len * len(words)

        if len(s) < right:
            return output
        
        temp_word = words[:]

        while right <= len(s):
            if s[left:left+words_len] in words_set:
                if left > 0 and not len(temp_word) and s[left-1] in words_set and s[left-1] == s[right-1]:
                    output.append(left)
                else:
                    temp_word = words[:]
                    check_i = left
                    for i in range(len(temp_word)):
                        word = s[check_i:check_i+words_len]
                        if word in temp_word:
                            temp_word.remove(word)
                            check_i += words_len
                        else:
                            break
                
                    if not len(temp_word):
                        output.append(left)
                
            left += 1
            right += 1


        return output

obj = Solution()
print(obj.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
print(obj.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
print(obj.findSubstring("a",["a"]))
print(obj.findSubstring("aaa",["a","a"]))
print(obj.findSubstring("bcabbcaabbccacacbabccacaababcbb",["c","b","a","c","a","a","a","b","c"]))