class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = set()

        pos = []
        neg = []
        zero = []

        for num in nums:
            if num > 0:
                pos.append(num)
            elif num< 0:
                neg.append(num)
            else:
                zero.append(num)
        
        if len(zero) >= 3:
            output.add(tuple([0,0,0]))

        pos_set = set(pos)
        neg_set = set(neg)

        if len(zero):
            for i in range(len(pos)):
                if -1 * (pos[i]) in neg_set:
                    output.add(tuple(sorted([pos[i], 0, -1 * (pos[i])])))

            for i in range(len(neg)):
                if -1 * (neg[i]) in pos_set:
                    output.add(tuple(sorted([neg[i], 0, -1 * (neg[i])])))

        for i in range(len(pos)-1):
            for j in range(i+1, len(pos)):
                if -1 * (pos[i] + pos[j]) in neg_set:
                    output.add(tuple(sorted([pos[i], pos[j], -1 * (pos[i] + pos[j])])))

        for i in range(len(neg)-1):
            for j in range(i+1, len(neg)):
                if -1 * (neg[i] + neg[j]) in pos_set:
                    output.add(tuple(sorted([neg[i], neg[j], -1 * (neg[i] + neg[j])])))

        return output


obj = Solution()
print(obj.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]))
print(obj.threeSum([0,0,0]))
print(obj.threeSum([1,1,-2]))