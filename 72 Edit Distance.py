class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        # setup dp matrix
        dp = [[-1]*len(word2) for i in range(len(word1))]
        if word1[0] == word2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1,len(word1)):
            if word2[0] == word1[i]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i-1][0] + 1
        for j in range(1,len(word2)):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j-1] + 1

        def dp_setter(cur_i, cur_j):
            if dp[cur_i][cur_j] != -1:
                return dp[cur_i][cur_j]
            else:
                return dp_iter(cur_i, cur_j)

        def dp_iter(cur_i, cur_j):

            if cur_i > 0 and cur_j > 0 and word1[cur_i] == word2[cur_j]:
                dp[cur_i][cur_j] = dp_setter(cur_i-1, cur_j-1)
            else:
                letter_del, letter_ins, letter_rep = float('inf'), float('inf'), float('inf')
                if cur_i - 1 >= 0:
                    letter_del = dp_setter(cur_i-1, cur_j) + 1
                if cur_j - 1 >= 0:
                    letter_ins = dp_setter(cur_i, cur_j-1) + 1
                if cur_i - 1 >= 0 and cur_j - 1 >= 0:
                    letter_rep = dp_setter(cur_i-1, cur_j-1) + 1

                dp[cur_i][cur_j] = min(letter_del, letter_ins, letter_rep)

            return dp[cur_i][cur_j]
        
        if dp[len(word1)-1][len(word2)-1] != -1:
            return dp[len(word1)-1][len(word2)-1]
        else:
            return dp_iter(len(word1)-1, len(word2)-1)

obj = Solution()
# print(obj.minDistance("sea", "eat"))
# print(obj.minDistance("horse", "ros"))
print(obj.minDistance("zoologicoarchaeologist", "zoogeologist"))