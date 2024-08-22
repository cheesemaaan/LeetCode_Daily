class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        answer = 0
        up_count = commands.count("UP")
        down_count = commands.count("DOWN")
        left_count = commands.count("LEFT")
        right_count = commands.count("RIGHT")
        answer += right_count
        answer -= left_count
        answer += down_count*n
        answer -= up_count*n
        return answer
