class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # answer = True
      
        if int(str(num)[-1])!=0 or num==0 :
            return True
        else: return False