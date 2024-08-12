class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        check = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
            
                if prices[i]>=prices[j]:
                    check.append(prices[i]-prices[j])
                    
                    continue
                    
                else:
                    continue
           
            if check == []:
                answer.append(prices[i])
            else:
                answer.append(check[0])
            check = []
        return answer
