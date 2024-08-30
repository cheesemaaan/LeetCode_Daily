class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        answer = []
        for i in range(1,n):
            a=i
            b=n-i
            if '0' not in str(a)+str(b):
                answer.append(a)
                answer.append(b)
                return answer
            else:
                continue
        return answer
