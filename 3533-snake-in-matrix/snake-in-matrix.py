# class Solution:
#     def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
#         answer = 0
#         up_count = commands.count("UP")
#         down_count = commands.count("DOWN")
#         left_count = commands.count("LEFT")
#         right_count = commands.count("RIGHT")
#         answer += right_count
#         answer -= left_count
#         answer += down_count*n
#         answer -= up_count*n


#         return answer


# class Solution:
#     def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
#         answer = 0
#         up_count = down_count = left_count = right_count = 0

#         for command in commands:
#             if command == "UP":
#                 up_count += 1
#             elif command == "DOWN":
#                 down_count += 1
#             elif command == "LEFT":
#                 left_count += 1
#             elif command == "RIGHT":
#                 right_count += 1

#         answer += right_count
#         answer -= left_count
#         answer += down_count * n
#         answer -= up_count * n

#         return answer

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        return sum(1 if cmd == "RIGHT" else -1 if cmd == "LEFT" else n if cmd == "DOWN" else -n for cmd in commands)
