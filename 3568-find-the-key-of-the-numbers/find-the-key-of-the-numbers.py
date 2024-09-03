class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        answer =""
        str_1 = str(num1).zfill(4) 
        str_2 = str(num2).zfill(4)
        str_3 = str(num3).zfill(4)
        for c in zip(str_1,str_2,str_3):
            answer += min(c)  # 각 자릿수의 문자열 모음인 튜플형태이므로  min함수 적용가능한 점 기억하기!
        answer = answer.lstrip('0') or '0'
        return int(answer)