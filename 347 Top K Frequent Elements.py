class Solution:
    def topKFrequent(self, nums, k: int):
        fre_dict = {}
        for num in nums:
            if num not in fre_dict:
                fre_dict[num] = 1
            else:
                fre_dict[num] += 1
        
        return [num[0] for num in list(sorted(fre_dict.items(), key = lambda item: item[1]))[::-1][:k]]