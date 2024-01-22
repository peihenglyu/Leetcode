class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dict = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        output = []
        def solver(index, letters):
            if index == len(digits)-1:
                for letter in num_dict[int(digits[index])]:
                    output.append(letters+letter)
            else:
                for letter in num_dict[int(digits[index])]:
                    solver(index+1, letters + letter)
        
        if len(digits):
            solver(0,"")
            
        return output


obj = Solution()
print(obj.letterCombinations(""))
print(obj.letterCombinations("2"))
print(obj.letterCombinations("23"))