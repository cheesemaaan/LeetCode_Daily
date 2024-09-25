# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         sum_code = 0
#         answer=[0]*len(code)
#         if k == 0:
#             return answer
#         elif k>0:
#             for i in range(len(code)):
#                 for s in range(k):
#                     sum_code+=code[((i+s+1)%len(code))]
                    
                
#                 answer[i]=sum_code
#                 sum_code=0
#         elif k < 0:
#              for i in range(len(code)):
#                 for s in range(-k):
#                     sum_code+=code[((i-s-1)%len(code))]
#                 answer[i]=sum_code
#                 sum_code=0
        
#         return answer

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = [0] * n
        
        if k == 0:
            return answer
        
        for i in range(n):
            sum_code = 0
            if k > 0:
                for j in range(1, k + 1):
                    sum_code += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    sum_code += code[(i - j) % n]
            answer[i] = sum_code
        
        return answer
