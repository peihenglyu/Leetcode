class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        oc_set = set()
        num_dict = {}
        for n in arr:
            if n not in num_dict:
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        
        for key in num_dict:
            if num_dict[key] not in oc_set:
                oc_set.add(num_dict[key])
            else:
                return False
        
        return True