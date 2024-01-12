class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        dict_letter = {}
        for letter in s:
            if letter in dict_letter:
                dict_letter[letter] += 1
            else:
                dict_letter[letter] = 1
            
        count_list = []
        dict_index = {}

        list_letter = sorted(dict_letter.items(), key = lambda x:x[1], reverse = True)

        for i, pair in enumerate(list_letter):
            key = pair[0]
            value = pair[1]
            count_list.append(value)
            dict_index[i] = key
        
        if len(count_list) == 1 or count_list[0] > sum(count_list[1:]) + 1:
            return ""

        total = sum(count_list)
        round = 0

        result = ""
        while round < total:
            
            if count_list[0] > 0:
                result += dict_index[0]
                count_list[0] -= 1
                round += 1
            if count_list[1] > 0:
                result += dict_index[1]
                count_list[1] -= 1
                round += 1

            i = 2
            while i < len(count_list):
                if count_list[i] > count_list[i-1]:
                    if count_list[0] > count_list[i]:
                        result += dict_index[0] + dict_index[i]
                        count_list[0] -= 1
                        count_list[i] -= 1
                        round += 2
                    else:
                        result += dict_index[i]
                        count_list[i] -= 1
                        round += 1
                i += 1

        return result

    
obj = Solution()
print(obj.reorganizeString("a"))
print(obj.reorganizeString("aaaaabbbccd"))
print(obj.reorganizeString("aaaabbbbccccd"))
print(obj.reorganizeString("aaaabbbbb"))
print(obj.reorganizeString("aaaabb"))