class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        next_fizz = 1
        next_buzz = 1
        next_fizzbuzz = 1
        result = []
        for i in range(1,n+1):
            if i == next_fizzbuzz * 15:
                result.append("FizzBuzz")
                next_fizzbuzz += 1
                next_fizz += 1
                next_buzz += 1
            elif i == next_fizz * 3:
                result.append("Fizz")
                next_fizz += 1
            elif i == next_buzz * 5:
                result.append("Buzz")
                next_buzz += 1
            else:
                result.append(str(i))
        
        return result
    