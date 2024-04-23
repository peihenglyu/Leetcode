# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         dp = [0] * (len(s) + 1)
#         wordset = set(wordDict)
        
#         def solver(start):
#             index = start
#             while index < len(s):
#                 word = s[start:index+1]
#                 if word in wordset:
#                     if not dp[index+1]:
#                         dp[index+1] = 1
#                         solver(index+1)
#                 index += 1

#         solver(0)

#         return dp[-1]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """ 

        dp = [False] * (len(s))
        
        for i in range(len(s)):
            for word in wordDict:
                
                if i < len(word) - 1:
                    continue

                if dp[i-len(word)] or i == len(word) - 1:
                    if s[i-len(word)+1: i+1] == word:
                        dp[i] = True
                        break
                        
        print(dp)

        return dp[-1]

obj = Solution()
print(obj.wordBreak("leetcode", ["leet","code"]))
print(obj.wordBreak("applepenapple", ["apple","pen"]))
print(obj.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))