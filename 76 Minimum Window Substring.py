class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dict_t = {}
        output_len = float("inf")
        output = ""
        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 1
            else:
                dict_t[letter] += 1

        left = 0
        right = 0
        t_set = set(t)
        t_len = len(t_set)
        fill_count = 0

        while right < len(s):
            cur_letter = s[right]
            if cur_letter in t_set:
                dict_t[cur_letter] -= 1
                if dict_t[cur_letter] == 0:
                    fill_count += 1
            

            # if (cur_letter not in t_set) or (dict_t[cur_letter] < 0 and cur_letter == s[left]):
            while left < right and ((s[left] not in t_set) or (dict_t[s[left]] < 0 )) :
                if s[left] not in t_set:
                    left += 1
                else:
                    dict_t[s[left]] += 1
                    left += 1
                
            right += 1

            if fill_count == t_len:
                cur_output = s[left:right]
                if len(cur_output) < output_len:
                    output = cur_output
                    output_len = len(cur_output)

        return output
    

obj = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(obj.minWindow(s,t))
print(obj.minWindow("a","a"))
print(obj.minWindow("a","aa"))
print(obj.minWindow("ab","b"))