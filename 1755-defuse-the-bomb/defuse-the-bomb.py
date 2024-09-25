class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        sum_code = 0
        answer=[0]*len(code)
        if k == 0:
            return answer
        elif k>0:
            for i in range(len(code)):
                for s in range(k):
                    sum_code+=code[((i+s+1)%len(code))]
                    print(sum_code)
                
                answer[i]=sum_code
                sum_code=0
        elif k < 0:
             for i in range(len(code)):
                for s in range(-k):
                    sum_code+=code[((i-s-1)%len(code))]
                answer[i]=sum_code
                sum_code=0
        print(answer)
        return answer
                
