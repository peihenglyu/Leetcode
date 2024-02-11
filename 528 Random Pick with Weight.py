import bisect
from random import randint

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        
        sum_list = []
        cur_sum = 0
        for num in w:
            cur_sum += num
            sum_list.append(cur_sum)
        self.sum_list = sum_list
        

    def pickIndex(self):
        """
        :rtype: int
        """

        rand = randint(1,self.sum_list[-1])
        
        return bisect.bisect_left(self.sum_list,rand)
           


# Your Solution object will be instantiated and called as such:
# obj = Solution([1,3])
# param_1 = obj.pickIndex()
# print(param_1)
# param_1 = obj.pickIndex()
# print(param_1)
# param_1 = obj.pickIndex()
# print(param_1)
# param_1 = obj.pickIndex()
# print(param_1)
# param_1 = obj.pickIndex()
# print(param_1)