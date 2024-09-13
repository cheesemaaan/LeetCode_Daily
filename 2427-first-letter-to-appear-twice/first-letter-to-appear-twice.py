class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count_dict = {}
        for i,c in enumerate(s):
            if c not in count_dict:
                count_dict[c]=[i,1]
            else:
                return c
        
        

