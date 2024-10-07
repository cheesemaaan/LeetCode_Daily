class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num%divisor ==0:
                    score +=1
            d[divisor] = score
        
     
        score_max = max(d.values())
        return min(divisor for divisor,score in d.items() if score==score_max)

        
    