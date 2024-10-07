class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num%divisor ==0:
                    score+=1
            
            d[divisor] =score
        print(d)
        # max_score =max(d.values())
        # return min([divisor for divisor,score in d.items() if score==max_score])
        sorted_d = sorted(d.items(),key = lambda x : (-x[1],x[0]))
        return sorted_d[0][0]


    