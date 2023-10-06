class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        try_index = 0
        cur_gas = gas[try_index]
        while try_index < len(gas):
            step = 0
            print(f"try {try_index}")
            while step <= len(gas):
                if step == len(gas):
                    return try_index
                print(f"test at {(try_index+step)%len(gas)}")
                cur_gas -= cost[(try_index+step)%len(gas)]
                print(f"cur_gas:{cur_gas}")
                if cur_gas < 0:
                    print(f"since cur_gas < 0, set try_index = {try_index} + {step} + 1 = {try_index + step}")
                    try_index += step+1
                    cur_gas = gas[try_index%len(gas)]
                    break
                step += 1
                cur_gas += gas[(try_index+step)%len(gas)]
        return -1
    
class candySolution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy_sum = 0
        i = 0
        step = 1
        First_Child = True
        last_child = 0
        while i < len(ratings):
            while i + step < len(ratings) and ratings[i + step] < ratings[i + step - 1]:
                print(f"i:{i}, step:{step}")
                step += 1

            if step == 1 and First_Child:
                print(f"give candy:{[1]}")
                candy_sum += 1
                First_Child = False
                last_child = 1
            elif step == 1 and ratings[i + step -1] > ratings[i + step - 2]:
                candy_amount = last_child + 1
                print(f"give candy:{[candy_amount]}")
                candy_sum += candy_amount
                last_child = candy_amount
            elif step == 1 and ratings[i + step -1] == ratings[i + step - 2]:
                candy_amount = 1
                print(f"give candy:{[candy_amount]}")
                candy_sum += candy_amount
                last_child = candy_amount
            elif ratings[i] > ratings[i - 1]:
                print(f"{ratings[i]} > {ratings[i - 1]}")
                candy_list = list(range(1,step+1))
                candy_list[-1] = max(candy_list[-1],last_child + 1)
                print(f"give candy:{candy_list[::-1]}")
                candy_sum += sum(candy_list)
                First_Child = False
                last_child = 1
            else:
                print(f"{ratings[i]} <= {ratings[i - 1]}")
                candy_list = list(range(1,step+1))
                print(f"give candy:{candy_list[::-1]}")
                candy_sum += sum(candy_list)
                First_Child = False
                last_child = 1
            i = i + step
            step = 1

        return candy_sum
    

class rainSolution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_rain = 0
        stack = []
        for i in range(len(height)):
            if height[i] > 0 and i != 0:
                # if height[i] - height[i-1] > 0:
                end_diff = height[i] - height[i-1]
                if end_diff > 0:
                    while end_diff > 0 and len(stack) > 0:
                        print("end rain")
                        if end_diff >= stack[-1][1]:
                            end_diff -= stack[-1][1]
                            total_rain += (i - stack[-1][0] - 1) * stack[-1][1]
                            stack.pop()
                        else:
                            total_rain += (i - stack[-1][0] - 1) * end_diff
                            stack[-1] = (stack[-1][0], stack[-1][1] - end_diff)
                            end_diff = 0
                        print(f"stack: {stack}, total_rain: {total_rain}")


            if height[i] > 0 and i != len(height)-1:
                # if height[i] - height[i + 1] > 0:
                start_diff = height[i] - height[i + 1]
                if start_diff > 0:
                    stack.append((i,start_diff))

            print(f"index:{i} stack: {stack}, total_rain: {total_rain}")
        return total_rain

class Solution12(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        letter_list = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        num_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for i in range(len(num_list)):
            print(f"if {num} % {num_list[i]} != 0")
            if int(num / num_list[i]) != 0:
                n_letter = int(num/num_list[i])
                roman += letter_list[i] * n_letter
                num = num % num_list[i]

        return roman


obj_12 = Solution12()

print(obj_12.intToRoman(3))