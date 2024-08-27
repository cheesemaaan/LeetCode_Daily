class Solution:
    def makeFancyString(self, s: str) -> str:
            result = []  # 빈 리스트로 시작
            for char in s:
        # 현재 문자를 추가할지 결정하기 위해 리스트의 길이를 확인
                if len(result) < 2 or not (char == result[-1] == result[-2]):
                    result.append(char)
            return ''.join(result)

