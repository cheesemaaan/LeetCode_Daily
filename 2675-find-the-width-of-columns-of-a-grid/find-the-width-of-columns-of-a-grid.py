class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer =[]
        for i in range(len(grid[0])):
            max_length =0 # 같은 칼럼만 얻기 위해 print때순서반대로!
            for j in range(len(grid)):
                max_length = max(len(str(grid[j][i])),max_length)
            
            answer.append(max_length)
        
        return answer
                