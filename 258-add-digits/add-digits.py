class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        
        while num>=10:
                answer = 0
                for i in str(num):
                    answer += int(i)
            
                num = answer 
                if answer < 10:
                    return answer
                    
           
        