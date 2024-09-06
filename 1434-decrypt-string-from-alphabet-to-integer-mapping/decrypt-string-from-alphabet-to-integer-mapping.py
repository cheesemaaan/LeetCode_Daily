# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         cha_dict = {}
#         alphabet = list(string.ascii_lowercase)
        
#         for i,c in enumerate(alphabet):
#             if i+1 < 10:
#                 cha_dict[f"{i+1}"] = c
#             else:
#                 cha_dict[f"{i+1}"+"#"] = c
#         print(cha_dict)
#         result = []

#         i = 0
#         while i < len(s):
#             # 뒤에서부터 탐색하면서 '10#'-'26#'을 먼저 처리
#             if i + 2 < len(s) and s[i + 2] == '#':
#                 # '10#'-'26#' 형태
#                 num = s[i:i+3]  # 세 문자를 가져옴 (예: '10#')
#                 result.append(cha_dict[num])  # 해당 숫자에 맞는 알파벳 추가
#                 i += 3  # 세 글자를 처리했으므로 인덱스를 3만큼 이동
#             else:
#                 # '1'-'9' 형태
#                 num = s[i]  # 한 문자를 가져옴 (예: '2')
#                 result.append(cha_dict[num])  # 해당 숫자에 맞는 알파벳 추가
#                 i += 1  # 한 글자를 처리했으므로 인덱스를 1만큼 이동

#         # 리스트를 문자열로 변환하여 반환
#         return ''.join(result)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        n = len(s)

        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                # '10#'-'26#' 처리
                num = s[i:i + 2]  # 두 자리 숫자
                result.append(chr(int(num) + 96))  # 숫자를 알파벳으로 변환
                i += 3  # 세 문자를 처리했으므로 인덱스를 3만큼 이동
            else:
                # '1'-'9' 처리
                result.append(chr(int(s[i]) + 96))  # 한 자리 숫자를 알파벳으로 변환
                i += 1  # 한 글자를 처리했으므로 인덱스를 1만큼 이동

        return ''.join(result)
