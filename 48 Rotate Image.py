class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
            
        n = len(matrix[0])
        for i in range(n//2):
            for j in range(0+i, n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        return matrix
            
obj = Solution()
print(obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(obj.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))