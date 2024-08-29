class Solution:
    def reformatNumber(self, number: str) -> str:
        answer =[]
        number = number.replace("-","").replace(" ", "")
        while len(number) >=5:
            if len(number)>=4:
                answer.append(number[:3])
                number= number[3:]
                
        
        if len(number) == 3 or len(number) == 2:
            answer.append(number)
        elif len(number) == 4:
            answer.append(number[:2])
            answer.append(number[2:])
        
        return "-".join(answer)

      