class Solution:
    def clearDigits(self, s: str) -> str:
        result = []  # 결과를 저장할 리스트
        i = 0
        while i < len(s):
            if s[i].isdigit():  # 숫자를 발견하면
                if result:  # 리스트가 비어있지 않다면
                    result.pop()  # 숫자 앞의 문자를 제거
            else:
                result.append(s[i])  # 숫자가 아닌 문자는 결과에 추가
            i += 1
        return ''.join(result)  # 리스트를 문자열로 변환하여 반환
