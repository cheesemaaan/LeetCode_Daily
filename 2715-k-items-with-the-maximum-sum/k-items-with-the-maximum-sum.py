class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0
        if k<(numOnes+numZeros):
            if numOnes>k:
                answer =k
            else:
                answer =numOnes
        else:
            answer +=(numOnes)-(k-(numOnes+numZeros))
        return answer
           