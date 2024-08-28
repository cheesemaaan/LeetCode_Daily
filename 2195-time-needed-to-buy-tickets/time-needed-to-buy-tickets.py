class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0 
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] < tickets[k]:
                    answer += tickets[i]
                else:
                    answer += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    answer +=tickets[i]
                else:
                    answer +=tickets[k]-1

        return answer



        