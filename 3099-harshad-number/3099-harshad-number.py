class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        number = 0
        for num in str(x):
            number += int(num)
        if x % number == 0:
            return number
        else:
            return -1
