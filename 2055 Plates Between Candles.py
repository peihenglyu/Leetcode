class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        output = []
        for query in queries:
            count = 0
            left = query[0]
            right = query[1]
            while left < len(s) and s[left] == "*":
                left += 1
            while right > 0 and s[right] == "*":
                right -= 1
            while left <= right:
                if left == right:
                    if s[left] == "*":
                        count += 1
                    left += 1
                    right -= 1
                else:
                    if s[left] == "*":
                        count += 1
                    left += 1
                    if s[right] == "*":
                        count += 1
                    right -= 1
            output.append(count)

        return output 

obj = Solution()
# print(obj.platesBetweenCandles("**|**|***|", [[2,5],[5,9]]))
print(obj.platesBetweenCandles("***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]]))