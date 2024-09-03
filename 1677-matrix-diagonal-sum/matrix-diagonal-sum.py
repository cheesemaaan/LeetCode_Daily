class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer =0
        n =len(mat)
        for i in range(len(mat)):
            answer +=mat[i][i]
            answer +=mat[i][n-1-i]
        middle = n//2
        if n%2 ==1:
            answer -= mat[middle][middle]
        return answer
