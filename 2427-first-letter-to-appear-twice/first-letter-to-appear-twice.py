class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count_dict = {}
        for i,c in enumerate(s):
            if c not in count_dict:
                count = 0
                count+=1
                count_dict[c]=[i,count]
            else:
                return c
        
        

