class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = list(strs)
        output=[]
        for i in range(len(strs)):
            sorted_strs[i] = (sorted(sorted_strs[i]),i)
        
        sorted_strs = sorted(sorted_strs, key=lambda x: x[0])

        cur_group = []
        cur_word = None
        for word in sorted_strs:
            if cur_word == None:
                cur_word = word[0]
                cur_group.append(strs[word[1]])
            elif cur_word == word[0]:
                cur_group.append(strs[word[1]])
            else:
                output.append(cur_group)
                cur_group = []
                cur_group.append(strs[word[1]])
                cur_word = word[0]
        output.append(cur_group)

        return output

obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))