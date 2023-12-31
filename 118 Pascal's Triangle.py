class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        if numRows == 1:
            return result
        
        result.append([1,1])
        if numRows == 2:
            return result
        
        for i in range(1, numRows-1):
            temp = [1]
            index = 0
            while index + 1 < len(result[i]):
                temp.append(result[i][index] + result[i][index + 1])
                index += 1
            temp.append(1)
            result.append(temp)

        return result
    
obj = Solution()
print(obj.generate(5))