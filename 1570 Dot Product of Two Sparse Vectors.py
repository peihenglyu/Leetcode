class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vec = nums        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        vec1 = self.vec
        vec2 = vec.vec
        dot_prod = 0
        for i in range(len(vec1)):
            if vec1[i] != 0 and vec2[i] != 0:
                dot_prod += vec1[i] * vec2[i]
        
        return dot_prod


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)