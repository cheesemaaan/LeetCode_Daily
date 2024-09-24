# class Solution:
#     def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
#         answer =[]
#         for i in range(len(grid[0])):
#             max_length =0 # 같은 칼럼만 얻기 위해 print때순서반대로!
#             for j in range(len(grid)):
#                 max_length = max(len(str(grid[j][i])),max_length)
            
#             answer.append(max_length)
        
#         return answer


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # 2중 for문, 숫자 -> 문자열로 변환
        answer = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num_len = len(str(grid[i][j]))
                answer[j] = max(answer[j], num_len)
        return answer
                