class Solution:
    def makeFancyString(self, s: str) -> str:
            result = s[0:2]  # 초기 두 문자(또는 그 이하)를 결과에 미리 추가
        
            for i in range(2, len(s)):
                # 마지막 두 문자와 현재 문자가 같지 않다면 결과에 추가
                if not (s[i] == result[-1] == result[-2]):
                    result += s[i]
        
            return result
