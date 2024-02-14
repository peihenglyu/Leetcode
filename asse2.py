class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        pin = []
        for index, letter in enumerate(s):
            if letter in ['a','e','i','o','u']:
                pin.append([letter, index])
        for i in range(len(pin)//2):
            temp = pin[i][1]
            pin[i][1] = pin[-(i+1)][1]
            pin[-(i+1)][1] = temp
        
        for i in range(len(pin)):
            s[pin[i][1]] = pin[i][0]
        
        return "".join(s)

obj = Solution()
print(obj.reverseVowels("hello"))
print(obj.reverseVowels("leetcode"))