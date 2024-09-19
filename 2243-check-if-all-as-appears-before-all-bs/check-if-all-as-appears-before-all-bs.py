class Solution:
    def checkString(self, s: str) -> bool:
        answer = True
        for i in range(1,len(s)):
            if  s[i-1] == 'b' and s[i] =='a':
               
                answer = False
        
        return answer