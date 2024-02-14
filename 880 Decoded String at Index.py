class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        count = 0
        right = 0

        for index in range(len(s)):
            i = s[index]
            if i.isalpha():
                count += 1
            else:
                count *= int(i)
            
            if count >= k:
                if i.isalpha():
                    return i
                else:
                    rest = k
                    back_index = index
                    while rest != 0:
                        back_i = s[back_index]

                        if back_i.isalpha():
                            if count > rest:
                                count -= 1
                            else:
                                return back_i
                        else:
                            if rest > count//int(back_i):
                                count = count//int(back_i)
                                rest = rest % (count)
                            else:
                                count = count//int(back_i)
                            
                        back_index -= 1
                    while s[back_index].isdigit():
                        back_index -= 1
                    return s[back_index]

        
        # count = 0
        # right = 0
        # tape = []
        # while count < rest:
        #     cur = s[right]
        #     if cur.isalpha():
        #         tape.append(cur)
        #         count += 1
        #         right += 1
        #     else:
        #         repeat = int(cur)-1
        #         cur_tape = tape[:]
        #         for i in range(repeat):
        #             for j in cur_tape:
        #                 tape.append(j)
        #                 count += 1
        #                 if count == rest:
        #                     return tape[count-1]
        #         right += 1
        
        # return tape[count-1]




obj = Solution()
# print(obj.decodeAtIndex("leet2code3", 10))
# print(obj.decodeAtIndex("ha22", 5))
# print(obj.decodeAtIndex("a23", 6))
print(obj.decodeAtIndex("abc33a", 27))
print(obj.decodeAtIndex("abc33", 27))
print(obj.decodeAtIndex("abc33", 9))
print(obj.decodeAtIndex("abc3a", 9))
# print(obj.decodeAtIndex("a2345678999999999999999", 1))
# print(obj.decodeAtIndex("y959q969u3hb22odq595", 222280369))