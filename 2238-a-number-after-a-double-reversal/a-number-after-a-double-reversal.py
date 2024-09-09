class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # answer = True
        if num==0:
            return True
        if abs(num) > 0 and int(str(num)[-1])!=0:
            return True
        else: return False